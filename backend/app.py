from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Simple in-memory data for now
companies_data = {
    "121006834": {
        "name": "Kishan Inc.",
        "license": "121006834",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "net_income": 17750.30,
        "state_share": 6212.61,
        "net_ach": 5637.20
    },
    "230701003": {
        "name": "MIRA'S GAMING CAFE ,LLC",
        "license": "230701003",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "net_income": 29204.53,
        "state_share": 10221.59,
        "net_ach": 9357.13
    },
    "240700017": {
        "name": "J & B One, Inc.",
        "license": "240700017",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "net_income": 17594.24,
        "state_share": 6157.98,
        "net_ach": 5637.19
    },
    "230701046": {
        "name": "7 STAR CAFE LLC",
        "license": "230701046",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "net_income": 17606.44,
        "state_share": 6162.25,
        "net_ach": 5641.10
    }
}

@app.route('/')
def home():
    return jsonify({
        'message': 'Midwest VG Solutions API',
        'status': 'running',
        'version': '1.0'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'midwest-vg-portal'
    })

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    license_number = data.get('license_number')
    password = data.get('password')
    
    if license_number in companies_data:
        company = companies_data[license_number]
        if company['password'] == password:
            return jsonify({
                'success': True,
                'company': {
                    'name': company['name'],
                    'license': company['license'],
                    'vgt_count': company['vgt_count']
                },
                'token': 'demo-token-123'
            })
    
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/api/admin/companies')
def get_companies():
    return jsonify({
        'companies': [
            {'name': c['name'], 'license': c['license'], 'vgt_count': c['vgt_count']}
            for c in companies_data.values()
        ]
    })

@app.route('/api/company/dashboard')
def get_dashboard():
    # For demo, return first company's data
    company = list(companies_data.values())[0]
    return jsonify({
        'company': {
            'name': company['name'],
            'license': company['license'],
            'vgt_count': company['vgt_count']
        },
        'latest_report': {
            'net_terminal_income': company['net_income'],
            'state_share': company['state_share'],
            'net_ach_deposit': company['net_ach']
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
