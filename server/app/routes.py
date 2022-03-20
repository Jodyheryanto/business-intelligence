from app import app
from app.controller import APIController
from app.controller import UserController
from app.controller import PostController
from app.controller import GooglePlayController
from app.controller import AppStoreController
from app.controller import TwitterController
from app.controller import InstagramController
from app.controller import WordCloudController
from app.controller import NotifController
from app.controller import HelpController
from flask import request
from app import response

@app.route('/getgoogleplay')
def view_googleplay():
    args = request.args
    if(len(args) == 4):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        user_id = int(args["user_id"])
        sentiment = args["sentiment"]
        sentiments = comma_separated_params_to_list(sentiment)
        if(user_id!='' and sentiment!='' and tanggal_akhir!='' and tanggal_awal!='' and user_id!=1):
            return GooglePlayController.printData(tanggal_awal, tanggal_akhir, sentiments, user_id)
        elif(user_id==1):
            return GooglePlayController.printAllData(tanggal_awal, tanggal_akhir, sentiments)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/rungoogleplay')
def run_googleplay():
    args = request.args
    if(len(args) == 2):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        if(tanggal_akhir!='' and tanggal_awal!=''):
            return GooglePlayController.index(tanggal_awal, tanggal_akhir)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/getinstagram')
def view_instagram():
    args = request.args
    if(len(args) == 4):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        user_id = int(args["user_id"])
        sentiment = args["sentiment"]
        sentiments = comma_separated_params_to_list(sentiment)
        if(user_id!='' and sentiment!='' and tanggal_akhir!='' and tanggal_awal!='' and user_id!=1):
            return InstagramController.printData(tanggal_awal, tanggal_akhir, sentiments, user_id)
        elif(user_id==1):
            return InstagramController.printAllData(tanggal_awal, tanggal_akhir, sentiments)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/runinstagram')
def run_instagram():
    args = request.args
    if(len(args) == 2):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        if(tanggal_akhir!='' and tanggal_awal!=''):
            return InstagramController.index(tanggal_awal, tanggal_akhir)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/getappstore')
def view_appstore():
    args = request.args
    if(len(args) == 4):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        user_id = int(args["user_id"])
        sentiment = args["sentiment"]
        sentiments = comma_separated_params_to_list(sentiment)
        if(user_id!='' and sentiment!='' and tanggal_akhir!='' and tanggal_awal!='' and user_id!=1):
            return AppStoreController.printData(tanggal_awal, tanggal_akhir, sentiments, user_id)
        elif(user_id==1):
            return AppStoreController.printAllData(tanggal_awal, tanggal_akhir, sentiments)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/runappstore')
def run_appstore():
    args = request.args
    if(len(args) == 2):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        if(tanggal_akhir!='' and tanggal_awal!=''):
            return AppStoreController.index(tanggal_awal, tanggal_akhir)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/gettwitter')
def view_twitter():
    args = request.args
    if(len(args) == 4):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        user_id = int(args["user_id"])
        sentiment = args["sentiment"]
        sentiments = comma_separated_params_to_list(sentiment)
        if(user_id!='' and sentiment!='' and tanggal_akhir!='' and tanggal_awal!='' and user_id!=1):
            return TwitterController.printData(tanggal_awal, tanggal_akhir, sentiments, user_id)
        elif(user_id==1):
            return TwitterController.printAllData(tanggal_awal, tanggal_akhir, sentiments)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/runtwitter')
def run_twitter():
    args = request.args
    if(len(args) == 2):
        tanggal_awal = args["tanggal_awal"]
        tanggal_akhir = args["tanggal_akhir"]
        if(tanggal_akhir!='' and tanggal_awal!=''):
            return TwitterController.index(tanggal_awal, tanggal_akhir)
        else:
            return response.ok([], "")
    return {"msg":"Please fill the correct url!"}, 400

def comma_separated_params_to_list(param):
    result = []
    for val in param.split(','):
        if val:
            result.append(val)
    return result

@app.route('/wordcloud')
def wordcloud():
    args = request.args
    if(len(args) == 1):
        user_id = args["user_id"]
        return WordCloudController.printData(user_id)
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['PUT', 'GET', 'DELETE'])
def usersDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)

@app.route('/users/password/<id>', methods=['PUT'])
def usersPass(id):
    if request.method == 'PUT':
        return UserController.updatePass(id)
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/users/ubahstatus/<id>', methods=['PUT'])
def usersStatus(id):
    if request.method == 'PUT':
        return UserController.updateStatus(id)

@app.route('/getpost/<id>')
def postDetail(id):
    return PostController.show(id)

@app.route('/')
def home():
    return {"msg":"Please fill the correct url!"}, 400

@app.route('/refresh', methods=['POST'])
def refresh():
    return UserController.refresh()

@app.route('/apiconfig', methods=['PUT', 'GET'])
def apiconfig():
    if request.method == 'GET':
        return APIController.index()

@app.route('/apiconfig/<id>')
def updateApi(id):
    return APIController.update(id)

@app.route('/notifications', methods=['POST', 'GET'])
def notifications():
    if request.method == 'GET':
        args = request.args
        if(len(args) == 1):
            user_id = args["user_id"]
            return NotifController.showbyuser(user_id)
        else:
            return NotifController.index()
    else:
        return NotifController.store()

@app.route('/notifications/<id>', methods=['PUT', 'GET', 'DELETE'])
def sudahBaca(id):
    if request.method == 'GET':
        return NotifController.sudahBaca(id)
    elif request.method == 'DELETE':
        return NotifController.delete(id)
    else:
        return NotifController.update(id)

@app.route('/helps', methods=['POST', 'GET'])
def helps():
    if request.method == 'GET':
        return HelpController.index()
    else:
        return HelpController.store()

@app.route('/helps/<id>', methods=['PUT', 'DELETE'])
def ubahHelp(id):
    if request.method == 'DELETE':
        return HelpController.delete(id)
    else:
        return HelpController.update(id)
