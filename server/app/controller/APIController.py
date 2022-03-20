from app.model.api_config import API_Config
from app import response, app
from flask import request
from app import db
import datetime
from flask_jwt_extended import *
from app import mail
from flask_mail import Message
from flask import render_template

@jwt_required
def index():
    try:
        apiconfig = API_Config.query.all()
        data = transform(apiconfig)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

def transform(apiconfig):
    array = []
    for i in apiconfig:
        array.append(singleTransform(i))
    return array

def singleTransform(apiconfig):
    data = {
        'id': apiconfig.id,
        'url_api': apiconfig.url_api,
        'param1': apiconfig.param1,
        'param2': apiconfig.param2,
        'consumer_key': apiconfig.consumer_key,
        'consumer_secret': apiconfig.consumer_secret,
        'access_token': apiconfig.access_token,
        'access_token_secret': apiconfig.access_token_secret
    }

    return data

@jwt_required
def update(id):
    try:
        url_api = request.json['url_api']
        param1 = request.json['param1']
        param2 = request.json['param2']
        consumer_key = request.json['consumer_key']
        consumer_secret = request.json['consumer_secret']
        access_token = request.json['access_token']
        access_token_secret = request.json['access_token_secret']

        apiconfig = API_Config.query.filter_by(id=id).first()
        apiconfig.url_api = url_api
        apiconfig.param1 = param1
        apiconfig.param2 = param2
        apiconfig.consumer_key = consumer_key
        apiconfig.consumer_secret = consumer_secret
        apiconfig.access_token = access_token
        apiconfig.access_token_secret = access_token_secret
        db.session.commit()
        return response.ok('', 'Successfully update data!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')