import sys
import os
from flask_mail import Mail, Message
import requests
import json


sys.path.append('/home/me/Workspace')

from flask import redirect, render_template, url_for, flash, request, Flask, send_file, jsonify, send_from_directory

BASE_URL = 'https://goisn.net/inspectup/rest'
USER_NAME = 'Jana'
USER_PASSWORD = 'ok4u2:Login'
COMPANY_KEY = 'inspectup'

app = Flask(__name__)

PATH = '/home/me/Workspace/paxton'
@app.route("/", methods = ['GET', 'POST'])
def index():

    #if request.method =='POST':
    params = {
        'after': '04/01/2020',
        # 'end': '2020-04-09T14:03:01.956Z'
    }
    res = requests.get(BASE_URL + '/orders', auth=(USER_NAME, USER_PASSWORD), params=params)
    orders = json.loads(res.text)

    for order in orders['orders']:
        res = requests.get(BASE_URL + '/order/{}'.format(order['id']), auth=(USER_NAME, USER_PASSWORD))
        detailed_order = json.loads(res.text)
        client_id = detailed_order['order']['client']

        res = requests.get(BASE_URL + '/client/{}'.format(client_id), auth=(USER_NAME, USER_PASSWORD))
        client_data = json.loads(res.text)

        first_name = client_data['client']['first']
        last_name = client_data['client']['last']
        email = client_data['client']['email']

        mobile = client_data['client']['mobilephone']


    params = {
        'after': '04/01/2020',
        #'end': '2020-04-09T14:03:01.956Z'
    }
    res = requests.get(BASE_URL + '/orders' , auth=(USER_NAME, USER_PASSWORD), params=params)
    orders = json.loads(res._content)

    for order in orders['orders']:
        res = requests.get(BASE_URL + '/order/{}'.format(order['id']), auth=(USER_NAME, USER_PASSWORD))
        detailed_order = json.loads(res._content)
        pass
    print(res)

    return render_template('index.html')

@app.route("/order/<id>", methods=['GET'])
def order(id):
    res = requests.get(BASE_URL + '/order/{}'.format(id), auth=(USER_NAME, USER_PASSWORD))
    detailed_order = json.loads(res.text)
    client_id = detailed_order['order']['client']

    res = requests.get(BASE_URL + '/client/{}'.format(client_id), auth=(USER_NAME, USER_PASSWORD))
    client_data = json.loads(res.text)

    first_name = client_data['client']['first']
    last_name = client_data['client']['last']
    email = client_data['client']['email']

    mobile = client_data['client']['mobilephone']

    return render_template('pdf.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)