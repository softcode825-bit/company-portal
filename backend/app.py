from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Company data with full financial details
companies_data = {
    "121006834": {
        "id": 1,
        "name": "Kishan Inc.",
        "license_number": "121006834",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "email": "jpatel4233@gmail.com",
        "last_login": None
    },
    "230701003": {
        "id": 2,
        "name": "MIRA'S GAMING CAFE ,LLC",
        "license_number": "230701003",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "email": None,
        "last_login": None
    },
    "240700017": {
        "id": 3,
        "name": "J & B One, Inc.",
        "license_number": "240700017",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "email": None,
        "last_login": None
    },
    "230701046": {
        "id": 4,
        "name": "7 STAR CAFE LLC",
        "license_number": "230701046",
        "password": "vgsolutions2026",
        "vgt_count": 6,
        "email": None,
        "last_login": None
    }
}

# Reports data
reports_data = [
    {
        "id": 1,
        "company_id": 1,
        "license_number": "121006834",
        "period_start": "2026-02-01",
        "period_end": "2026-02-15",
        "net_terminal_income": 17750.30,
        "state_share": 6212.61,
        "net_ach_deposit": 5637.20,
        "funds_in": 41456.20,
        "funds_out": 23705.90,
        "amt_played": 107794.46,
        "amt_won": 90044.23,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 2,
        "company_id": 1,
        "license_number": "121006834",
        "period_start": "2026-02-16",
        "period_end": "2026-02-28",
        "net_terminal_income": 17666.76,
        "state_share": 6183.37,
        "net_ach_deposit": 5660.04,
        "funds_in": 42000.00,
        "funds_out": 24333.24,
        "amt_played": 110000.00,
        "amt_won": 92333.24,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 3,
        "company_id": 2,
        "license_number": "230701003",
        "period_start": "2026-02-01",
        "period_end": "2026-02-15",
        "net_terminal_income": 29204.53,
        "state_share": 10221.59,
        "net_ach_deposit": 8757.13,
        "funds_in": 75000.00,
        "funds_out": 45795.47,
        "amt_played": 180000.00,
        "amt_won": 150795.47,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 4,
        "company_id": 2,
        "license_number": "230701003",
        "period_start": "2026-02-16",
        "period_end": "2026-02-28",
        "net_terminal_income": 30500.31,
        "state_share": 10675.11,
        "net_ach_deposit": 9162.52,
        "funds_in": 78000.00,
        "funds_out": 47499.69,
        "amt_played": 185000.00,
        "amt_won": 154499.69,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 5,
        "company_id": 3,
        "license_number": "240700017",
        "period_start": "2026-02-01",
        "period_end": "2026-02-15",
        "net_terminal_income": 17594.24,
        "state_share": 6157.98,
        "net_ach_deposit": 5637.19,
        "funds_in": 41000.00,
        "funds_out": 23405.76,
        "amt_played": 106000.00,
        "amt_won": 88405.76,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 6,
        "company_id": 3,
        "license_number": "240700017",
        "period_start": "2026-02-16",
        "period_end": "2026-02-28",
        "net_terminal_income": 20686.83,
        "state_share": 7240.39,
        "net_ach_deposit": 6628.09,
        "funds_in": 48000.00,
        "funds_out": 27313.17,
        "amt_played": 125000.00,
        "amt_won": 104313.17,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 7,
        "company_id": 4,
        "license_number": "230701046",
        "period_start": "2026-02-01",
        "period_end": "2026-02-15",
        "net_terminal_income": 17606.44,
        "state_share": 6162.25,
        "net_ach_deposit": 5641.10,
        "funds_in": 41500.00,
        "funds_out": 23893.56,
        "amt_played": 107500.00,
        "amt_won": 89893.56,
        "status": "available",
        "pdf_available": True
    },
    {
        "id": 8,
        "company_id": 4,
        "license_number": "230701046",
        "period_start": "2026-02-16",
        "period_end": "2026-02-28",
        "net_terminal_income": 20359.76,
        "state_share": 7125.92,
        "net_ach_deposit": 6523.17,
        "funds_in": 47000.00,
        "funds_out": 26640.24,
        "amt_played": 122000.00,
        "amt_won": 101640.24,
        "status": "available",
        "pdf_available": True
    }
]

@app.route('/')
def home():
    return jsonify({
        'message': 'Midwest VG Solutions API',
        'status': 'running',
        'version': '2.0'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'midwest-vg-portal',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    license_number = data.get('license_number')
    password = data.get('password')
    
    if not license_number or not password:
        return jsonify({'message': 'License number and password required'}), 400
    
    if license_number in companies_data:
        company = companies_data[license_number]
        if company['password'] == password:
            # Update last login
            company['last_login'] = datetime.now().isoformat()
            
            return jsonify({
                'token': f'demo-token-{license_number}',
                'company': {
                    'id': company['id'],
                    'name': company['name'],
                    'license_number': company['license_number'],
                    'vgt_count': company['vgt_count'],
                    'email': company['email']
                }
            })
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/company/dashboard', methods=['GET'])
def get_dashboard():
    # Get token from header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'No authorization token'}), 401
    
    # Extract license number from token (demo implementation)
    try:
        token = auth_header.split()[1]
        license_number = token.replace('demo-token-', '')
        
        if license_number not in companies_data:
            return jsonify({'message': 'Invalid token'}), 401
        
        company = companies_data[license_number]
        
        # Get latest report for this company
        company_reports = [r for r in reports_data if r['license_number'] == license_number]
        company_reports.sort(key=lambda x: x['period_end'], reverse=True)
        
        latest_report = company_reports[0] if company_reports else {
            'net_terminal_income': 0,
            'state_share': 0,
            'net_ach_deposit': 0,
            'period_start': None,
            'period_end': None
        }
        
        return jsonify({
            'company': {
                'name': company['name'],
                'license_number': company['license_number'],
                'vgt_count': company['vgt_count'],
                'last_login': company['last_login']
            },
            'latest_report': {
                'net_terminal_income': latest_report['net_terminal_income'],
                'state_share': latest_report['state_share'],
                'net_ach_deposit': latest_report['net_ach_deposit'],
                'period_start': latest_report['period_start'],
                'period_end': latest_report['period_end']
            },
            'reports': [{
                'id': r['id'],
                'period_start': r['period_start'],
                'period_end': r['period_end'],
                'net_terminal_income': r['net_terminal_income'],
                'net_ach_deposit': r['net_ach_deposit'],
                'status': r['status'],
                'pdf_available': r['pdf_available']
            } for r in company_reports]
        })
    
    except Exception as e:
        return jsonify({'message': 'Invalid token', 'error': str(e)}), 401

@app.route('/api/reports/search', methods=['POST'])
def search_reports():
    # Get token from header
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'No authorization token'}), 401
    
    try:
        token = auth_header.split()[1]
        license_number = token.replace('demo-token-', '')
        
        if license_number not in companies_data:
            return jsonify({'message': 'Invalid token'}), 401
        
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        # Get reports for this company
        company_reports = [r for r in reports_data if r['license_number'] == license_number]
        
        # Filter by date if provided
        if start_date:
            company_reports = [r for r in company_reports if r['period_start'] >= start_date]
        
        if end_date:
            company_reports = [r for r in company_reports if r['period_end'] <= end_date]
        
        # Sort by date descending
        company_reports.sort(key=lambda x: x['period_end'], reverse=True)
        
        return jsonify({
            'reports': [{
                'id': r['id'],
                'period_start': r['period_start'],
                'period_end': r['period_end'],
                'net_terminal_income': r['net_terminal_income'],
                'net_ach_deposit': r['net_ach_deposit'],
                'status': r['status'],
                'pdf_available': r['pdf_available']
            } for r in company_reports]
        })
    
    except Exception as e:
        return jsonify({'message': 'Error searching reports', 'error': str(e)}), 500

@app.route('/api/admin/companies')
def get_companies():
    return jsonify({
        'companies': [{
            'id': c['id'],
            'name': c['name'],
            'license_number': c['license_number'],
            'vgt_count': c['vgt_count'],
            'last_login': c['last_login']
        } for c in companies_data.values()]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
