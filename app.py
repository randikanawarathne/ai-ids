import json
import random
import threading
import time
from datetime import datetime
from flask import Flask, render_template, jsonify, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ai-ids-secret-key-2024'
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=60, ping_interval=25)

class NetworkSimulator:
    def __init__(self):
        self.running = False
        self.thread = None
        self.events = []
        self.stats = {
            'total_packets': 0,
            'threats_detected': 0,
            'blocked_attacks': 0,
            'normal_traffic': 0
        }
        self.attack_types = ['DoS', 'Probe', 'R2L', 'U2R', 'Normal']
        self.ips = [
            '192.168.1.100', '192.168.1.101', '192.168.1.102',
            '10.0.0.50', '10.0.0.51', '172.16.0.10',
            '45.33.32.156', '104.16.249.249', '8.8.8.8',
            '1.1.1.1', '208.67.222.222'
        ]
        self.ports = [22, 80, 443, 3306, 8080, 21, 25, 53, 8081]
        self.protocols = ['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS', 'SSH', 'FTP']
        self.countries = ['US', 'CN', 'RU', 'DE', 'UK', 'JP', 'BR', 'IN', 'AU']
        
    def generate_event(self):
        is_threat = random.random() < 0.15
        attack_type = random.choice(self.attack_types)
        
        if is_threat:
            attack_type = random.choice(['DoS', 'Probe', 'R2L', 'U2R'])
            self.stats['threats_detected'] += 1
            if random.random() < 0.7:
                self.stats['blocked_attacks'] += 1
        else:
            self.stats['normal_traffic'] += 1
        
        self.stats['total_packets'] += 1
        
        src_ip = random.choice(self.ips)
        if is_threat and random.random() < 0.6:
            src_ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        
        event = {
            'id': self.stats['total_packets'],
            'timestamp': datetime.now().isoformat(),
            'src_ip': src_ip,
            'dst_ip': random.choice(self.ips),
            'src_port': random.randint(1024, 65535),
            'dst_port': random.choice(self.ports),
            'protocol': random.choice(self.protocols),
            'attack_type': attack_type,
            'risk_score': random.randint(0, 100) if is_threat else random.randint(0, 20),
            'bytes': random.randint(64, 1500),
            'country': random.choice(self.countries),
            'status': 'blocked' if is_threat and random.random() < 0.7 else 'allowed'
        }
        
        self.events.insert(0, event)
        if len(self.events) > 100:
            self.events = self.events[:100]
            
        return event

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()
        
    def _run(self):
        while self.running:
            event = self.generate_event()
            socketio.emit('new_event', event)
            socketio.sleep(2)
            
    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

simulator = NetworkSimulator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    return jsonify(simulator.stats)

@app.route('/api/events')
def get_events():
    return jsonify(simulator.events[:50])

@app.route('/api/chart-data')
def get_chart_data():
    labels = []
    normal_data = []
    threat_data = []
    
    for i in range(10, -1, -1):
        labels.append(f"{i*2}s ago")
        normal_data.append(random.randint(50, 200))
        threat_data.append(random.randint(0, 20))
        
    return jsonify({
        'labels': labels,
        'normal': normal_data,
        'threats': threat_data
    })

@app.route('/api/attack-distribution')
def get_attack_distribution():
    return jsonify({
        'DoS': random.randint(20, 40),
        'Probe': random.randint(15, 30),
        'R2L': random.randint(10, 25),
        'U2R': random.randint(5, 15),
        'Normal': random.randint(100, 200)
    })

@app.route('/api/threat-level')
def get_threat_level():
    threat = random.choice(['low', 'medium', 'high', 'critical'])
    return jsonify({'level': threat})

@app.route('/api/system-status')
def get_system_status():
    return jsonify({
        'cpu': random.randint(10, 60),
        'memory': random.randint(30, 70),
        'network_in': random.randint(100, 1000),
        'network_out': random.randint(50, 500),
        'uptime': random.randint(3600, 86400)
    })

@socketio.on('connect')
def handle_connect():
    emit('connection', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    pass

if __name__ == '__main__':
    simulator.start()
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
