import requests
import json
import sys

# Function to call an API 
def call_api(schema, body, headers, method):
	try:
		response = requests.request(method= method, url= schema, headers= headers, data= json.dumps(body))
		body_response = json.loads(response.text) # Convert string into json
		headers_response  = response.headers
		status_code = response.status_code
		return status_code, body_response, headers_response
	except Exception as e:
		print (e)
		sys.exit()

# API information
schema = "" 
body = {}
headers = {}
method = ""
exceped_code = 0

res_code, res_body, res_headers = call_api(schema, body, headers, method)

if res_code == exceped_code:
	# Code for succesfully test
else:
	# Code for failed test
