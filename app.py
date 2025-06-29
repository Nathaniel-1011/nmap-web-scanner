from flask import Flask, render_template, request, send_from_directory, jsonify
import datetime
import nmap
import os

app = Flask(__name__)

SCAN_REPORTS_DIR = "scan_reports"
os.makedirs(SCAN_REPORTS_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    report_filename = None
    timestamp = None
    os_info = None

    if request.method == 'POST':
        ip = request.form['ip']
        ports = request.form['ports']
        scanner = nmap.PortScanner()

        try:
            scanner.scan(ip, ports, arguments='-sS -sV -O')
            if ip not in scanner.all_hosts():
                output = "❌ Host unreachable or down."
            else:
                result = []
                # OS detection
                osmatches = scanner[ip].get('osmatch', [])
                if osmatches:
                    os_info = osmatches[0]['name']
                    result.append(f"OS Guess: {os_info}")
                else:
                    os_info = "Unknown"
                    result.append("OS Guess: Unknown")

                for proto in scanner[ip].all_protocols():
                    ports_list = scanner[ip][proto].keys()
                    for port in sorted(ports_list):
                        port_info = scanner[ip][proto][port]
                        service = port_info.get('name', 'unknown')
                        state = port_info['state'].upper()
                        product = port_info.get('product', '')
                        version = port_info.get('version', '')
                        extrainfo = port_info.get('extrainfo', '')
                        # Port as heading, details below
                        desc = [f"{proto.upper()} PORT {port}"]
                        desc.append(f"  Service: {service}")
                        desc.append(f"  Status: {state}")
                        if product:
                            desc.append(f"  Product: {product}")
                        if version:
                            desc.append(f"  Version: {version}")
                        if extrainfo:
                            desc.append(f"  Info: {extrainfo}")
                        result.append('\n'.join(desc))
                output = "\n\n".join(result)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%I-%M-%S_%p')
                report_filename = f"scan_{ip}_{timestamp}.txt"
                with open(f"{SCAN_REPORTS_DIR}/{report_filename}", 'w') as f:
                    f.write(output)

        except Exception as e:
            output = f"❌ Error: {str(e)}"

    # Pass current time in 12hr format with seconds
    current_time = datetime.datetime.now().strftime('%I:%M:%S %p')

    return render_template(
        "index.html",
        output=output,
        report_filename=report_filename,
        timestamp=timestamp,
        os_info=os_info,
        current_time=current_time
    )

@app.route('/download/<filename>')
def download_report(filename):
    return send_from_directory(SCAN_REPORTS_DIR, filename, as_attachment=True)

@app.route('/history')
def history():
    files = sorted(os.listdir(SCAN_REPORTS_DIR), reverse=True)
    return render_template("history.html", files=files)

@app.route('/report/<filename>')
def view_report(filename):
    path = os.path.join(SCAN_REPORTS_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        return jsonify({'content': content})
    return jsonify({'content': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
