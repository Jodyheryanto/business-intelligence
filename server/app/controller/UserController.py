from app.model.user import Users
from app.model.notification import Notifications
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
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')


def transform(users):
    array = []
    for i in users:
        array.append(singleTransform(i))
    return array

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')

        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email,
        'app_google_play': users.app_google_play,
        'app_apps_store': users.app_apps_store,
        'keyword_ig': users.keyword_ig,
        'keyword_twitter': users.keyword_twitter,
        'nama_aplikasi': users.nama_aplikasi,
        'description': users.description,
        'is_active': users.is_active,
        'success': True
    }

    return data

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        nama_aplikasi = request.json['nama_aplikasi']
        app_google_play = request.json['app_google_play']
        app_apps_store = request.json['app_apps_store']
        keyword_ig = request.json['keyword_ig']
        keyword_twitter = request.json['keyword_twitter']
        description = request.json['description']
        is_active = request.json['is_active']
        
        users_count = Users.query.filter_by(email=email).count()
        
        if(users_count == 0):
            users = Users(name=name, email=email, nama_aplikasi= nama_aplikasi, app_google_play=app_google_play, app_apps_store=app_apps_store, keyword_ig=keyword_ig, keyword_twitter=keyword_twitter, description=description, is_active=is_active)
            users.setPassword(password)
            db.session.add(users)
            db.session.commit()
            return response.ok('', 'You create an account and please wait until your account is beeing accepted!')
        else:
        	return response.badRequest('', 'Your Email is duplicated!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

@jwt_required
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']                
        nama_aplikasi = request.json['nama_aplikasi']
        app_google_play = request.json['app_google_play']
        app_apps_store = request.json['app_apps_store']
        keyword_ig = request.json['keyword_ig']
        keyword_twitter = request.json['keyword_twitter']
        description = request.json['description']
        is_active = request.json['is_active']

        user = Users.query.filter_by(id=id).first()

        user.email = email
        user.name = name
        user.nama_aplikasi = nama_aplikasi
        user.app_google_play = app_google_play
        user.app_apps_store = app_apps_store
        user.keyword_ig = keyword_ig
        user.keyword_twitter = keyword_twitter
        user.description = description
        user.is_active = is_active
        db.session.commit()

        return response.ok('', 'Successfully update data!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

@jwt_required
def updatePass(id):
    try:
        password = request.json['password']
        new_password = request.json['new_password']

        user = Users.query.filter_by(id=id).first()

        if not user.checkPassword(password):
            return response.badRequest([], 'Password lama yang dimasukkan salah')
        else: 
            user.setPassword(new_password)
            db.session.commit()

            return response.ok('', 'Successfully update password!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

@jwt_required
def updateStatus(id):
    try:
        is_active = request.json['is_active']

        user = Users.query.filter_by(id=id).first()

        user.is_active = is_active
        db.session.commit()

        if(is_active == 1):
            msg = Message(subject="Konfirmasi pengajuan akun Lenna Analytic",
                        sender='no-reply@gmail.com',
                        recipients=[str(user.email)])
            msg.html = render_template('mail_approved.html', app_name="PT Sinergi Digital Teknologi", app_contact="info@lenna.ai", name=user.name, email=user.email)
            mail.send(msg)
            data_notif = Notifications.query.order_by(Notifications.id.desc()).first()
            if data_notif is None:
                id_notif = 1
            else:
                id_notif = data_notif.id + 1
            notifications = Notifications(notif_id=id_notif, user_id=id, title="Welcome to our website", description="Hello "+user.name+",<br> Welcome and Thank You for Becoming Our Member", status=0)
            db.session.add(notifications)
            db.session.commit()
        else:
            msg = Message(subject="Konfirmasi pengajuan akun Lenna Analytic",
                        sender='no-reply@gmail.com',
                        recipients=[str(user.email)])
            msg.html = render_template('mail_rejected.html', app_name="PT Sinergi Digital Teknologi", app_contact="info@lenna.ai", name=user.name, email=user.email)
            mail.send(msg)
        return response.ok('', 'Successfully update data!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

@jwt_required
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty....')

        db.session.delete(user)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

def login():
    try:
        email = request.json['email']
        password = request.json['password']

        user = Users.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Your username or password is not valid')

        if not user.checkPassword(password):
            return response.badRequest([], 'Your credentials is invalid')

        if(user.is_active != 0 and user.is_active != -1):
            data = singleTransform(user)
            expires = datetime.timedelta(minutes=60)
            expires_refresh = datetime.timedelta(minutes=60)
            access_token = create_access_token(data, fresh=True, expires_delta=expires)
            refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

            return response.ok({
                "data": data,
                "token_access": access_token,
                "token_refresh": refresh_token,
            }, "")
        elif(user.is_active == -1):
            return response.badRequest([], 'Your account is rejected by Administrator !')
        else: 
            return response.badRequest([], 'Your account not approve yet, please wait until approved in your email !')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')

@jwt_refresh_token_required
def refresh():
    try:
        user = get_jwt_identity()
        new_token = create_access_token(identity=user, fresh=False)

        return response.ok({
            "token_access": new_token
        }, "")

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')
