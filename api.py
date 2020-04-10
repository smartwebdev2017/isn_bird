import sys
import os
import requests
import json
from flask import render_template
from flask import Flask, request, jsonify

sys.path.append('/var/www')



BASE_URL = 'https://goisn.net/inspectup/rest'
USER_NAME = 'Jana'
USER_PASSWORD = 'ok4u2:Login'
COMPANY_KEY = 'inspectup'
BID = '156944290450716'
API_KEY = '5tEmf4QlEM0rpRiyGqxHxHGtYqa1nehG'

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    id = request.values['order_id']
    return render_template('index.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    if request.method == 'POST':
        id = request.values['order_id']

        res = requests.get(BASE_URL + '/order/{}'.format(id), auth=(USER_NAME, USER_PASSWORD))
        detailed_order = json.loads(res.text)
        try:
            client_id = detailed_order['order']['client']

            res = requests.get(BASE_URL + '/client/{}'.format(client_id), auth=(USER_NAME, USER_PASSWORD))
            client_data = json.loads(res.text)

            first_name = client_data['client']['first']
            last_name = client_data['client']['last']
            email = client_data['client']['email']

            mobile = client_data['client']['mobilephone']

            first_name = 'test'
            last_name = ''
            email = 'test@test.com'
            mobile = '408-xxx-xxxx'

            values = '{"name": "' + first_name + ' ' + last_name + '", "emailId": "' + email + '", "phone": "' + mobile + '", "smsEnabled": 1}'

            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
            res = requests.post(
                'https://api.birdeye.com/resources/v1/customer/checkin?bid={}&api_key={}'.format(BID, API_KEY), data=values,
                headers=headers)

        except Exception as e:
            pass

    return render_template('index.html')

@app.route("/order/<id>", methods=['GET'])
def order(id):
    res = requests.get(BASE_URL + '/order/{}'.format(id), auth=(USER_NAME, USER_PASSWORD))
    detailed_order = json.loads(res.text)
    try:
        client_id = detailed_order['order']['client']

        res = requests.get(BASE_URL + '/client/{}'.format(client_id), auth=(USER_NAME, USER_PASSWORD))
        client_data = json.loads(res.text)

        first_name = client_data['client']['first']
        last_name = client_data['client']['last']
        email = client_data['client']['email']

        mobile = client_data['client']['mobilephone']
    except Exception as e:
        pass

    first_name = 'test'
    last_name = ''
    email = 'test@test.com'
    mobile = '408-xxx-xxxx'

    values = '{"name": "' + first_name + ' ' + last_name + '", "emailId": "' + email + '", "phone": "' + mobile + '", "smsEnabled": 1}'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    request = requests.post('https://api.birdeye.com/resources/v1/customer/checkin?bid={}&api_key={}'.format(BID, API_KEY), data=values, headers=headers)

    return render_template('pdf.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
