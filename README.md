# 🔍 Nmap Web Scanner (Flask-based)

A professional web-based network scanner built with Python, Flask, and Nmap.  
Easily scan IP addresses and port ranges, view detailed results in your browser, and manage scan history with downloadable reports.

---

## 🚀 Features


SYN scan (-sS) with service & version detection (-sV)

User-defined port range

Detailed and clean output: service, state, product and  version.

Automatic timestamped report saving

Download and clipboard copy functionality in browser

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- python-nmap (Nmap wrapper)
- HTML/CSS (Jinja2 templates)
- Nmap (must be installed separately)

---

🌐 Frontend
Built with HTML and CSS (using Flask’s Jinja2 templating)

Simple form for input (target IP and port range)

Displays scan results and download link

📁 Files:

Templates/index.html

Static/style.css

🧠 Backend
Flask (Python web framework)

Handles routes and form submissions

Uses python-nmap to run and parse Nmap scans

Saves scan reports with timestamps in /reports/

📁 File:

app.py
File: app.py

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Nathaniel-1011/nmap-web-scanner.git
cd nmap-web-scanner
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Nmap

- **Windows:** Download and install from [nmap.org/download.html](https://nmap.org/download.html)
- **Linux:**  
  ```bash
  sudo apt-get install nmap
  ```
- **macOS:**  
  ```bash
  brew install nmap
  ```

### 4. Run the application
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🛡️ Disclaimer

This tool is intended for educational and authorized network security testing only.  
Do not scan networks or systems without proper permission.



