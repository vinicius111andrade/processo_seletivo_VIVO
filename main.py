from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/hello')
def hello_world():
	name = request.args.get('name')
	lastname = request.args.get('lastname')
	return_json = {
		"name" : name,
		"lastname" : lastname
	}
	return json.dumps(return_json)