from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Get our API keys from environment variables.
SHODAN_API_KEY = os.getenv('SHODAN_API_KEY') 
VIRUSTOTAL_API_KEY = os.getenv('VIRUSTOTAL_API_KEY') 

# https://nvd.nist.gov/developers/vulnerabilities
@app.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
	
	try:
		response = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0')
		vulnerabilities = response.json().get('vulnerabilities')

		if not vulnerabilities:
			return jsonify({'message': 'No vulnerabilities found.'}), 404
		return jsonify(vulnerabilities)
	
	except Exception as error:
		print('Error fetching vulnerabilities:', error)
		return jsonify({'message': 'Internal server error.'}), 500
	
if __name__ == '__main__':
	app.run(port=3000)