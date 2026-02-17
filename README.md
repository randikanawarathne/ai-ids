# AI-Driven Network Intrusion Detection System

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-green" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-yellow" alt="Python">
  <img src="https://img.shields.io/badge/status-Active-success" alt="Status">
</p>

> AI-powered network security monitoring system with real-time threat detection and interactive dashboard.

## Features

- Real-time network traffic monitoring and analysis
- AI-powered threat detection (DoS, Probe, R2L, U2R attacks)
- Modern dark-themed dashboard with cyber security aesthetic
- Live traffic visualization with Chart.js
- Attack alerts and notifications
- System resource monitoring (CPU, Memory, Network)
- Export reports for compliance
- WebSocket-powered real-time updates (server version)

## Screenshots

![Dashboard](screenshots/dashboard.png)

## Quick Start

### Option 1: Standalone (Browser Only)

Simply open `index.html` in your browser:
```bash
# Just open in browser - no installation needed
index.html
```

### Option 2: Full Server Version

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-ids.git
cd ai-ids

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Then open `http://127.0.0.1:5000` in your browser

## Project Structure

```
ai-ids/
├── index.html              # Standalone web version
├── app.py                  # Flask backend server
├── requirements.txt        # Python dependencies
├── SPEC.md                 # Project specification
├── deployment/             # Distribution package
│   ├── AI-IDS.bat
│   ├── config.json
│   └── templates/
├── .gitignore
├── LICENSE
└── README.md
```

## Requirements

### For Server Version
- Python 3.8 or higher
- Flask 3.0.0
- Flask-SocketIO 5.3.6
- Eventlet 0.34.2

### For Browser (Standalone)
- Modern web browser (Chrome, Firefox, Edge)
- No backend required

## Configuration

Edit `deployment/config.json`:

```json
{
  "app_name": "AI-IDS",
  "version": "1.0.0",
  "port": 5000,
  "threat_threshold": 15,
  "auto_start_monitoring": false,
  "data_retention_days": 30
}
```

## Usage

1. Launch the application
2. Click "Start Monitoring" to begin traffic simulation
3. Watch real-time threats appear in the live feed
4. Monitor threat levels and system resources
5. Export reports as needed

## API Endpoints (Server Version)

| Endpoint | Description |
|----------|-------------|
| `/api/stats` | Current statistics |
| `/api/events` | Recent traffic events |
| `/api/chart-data` | Traffic chart data |
| `/api/threat-level` | Current threat level |
| `/api/system-status` | System resources |
| `/api/attack-distribution` | Attack type breakdown |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Chart.js for visualizations
- Font Awesome for icons
- JetBrains Mono font

---

<p align="center">Made with 🔒 for network security</p>
