from app.model.notification import Notifications
from app.model.user import Users
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import *

@jwt_required
def index():
    try:
        notifs = Notifications.query.group_by(Notifications.notif_id).all()
        data = transform(notifs)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

@jwt_required
def showbyuser(user_id):
    try:
        notifs = Notifications.query.filter(Notifications.user_id==user_id).all()
        data = transform(notifs)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def transform(notifs):
    array = []
    for i in notifs:
        array.append(singleTransform(i))
    return array

@jwt_required
def show(id):
    try:
        posts = Posts.query.filter_by(id=id).first()
        if not posts:
            return response.ok([], 'Empty....')

        data = {
            'id' : posts.id,
            'user_name' : posts.user_name,
            'user_avatar' : posts.user_avatar,
            'post' : posts.post,
            'tanggal_post' : posts.tanggal_post.strftime('%Y-%m-%d'),
            'sumber' : posts.sumber,
            'aplikasi' : posts.aplikasi,
            'link_review' : posts.link_review,
            'rating' : posts.rating,
            'sentiment' : posts.sentiment
        }
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def singleTransform(notifs):
    data = {
        'id' : notifs.id,
        'title' : notifs.title,
        'description' : notifs.description,
        'tanggal_notif' : notifs.updated_at.strftime('%Y-%m-%d'),
        'status' : notifs.status
    }

    return data

def store():
    try:
        data_notif = Notifications.query.order_by(Notifications.id.desc()).first()
        if data_notif is None:
            id_notif = 1
        else:
            id_notif = data_notif.id + 1

        users = Users.query.all()
        
        for user in users: 
            notif_id = id_notif
            user_id = user.id
            title = request.json['title']
            description = request.json['description']
            status = 0

            notifications = Notifications(notif_id=notif_id, user_id=user_id, title=title, description=description, status=status)
            db.session.add(notifications)
            db.session.commit()

        return response.ok('', 'Successfully create data!')

    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def sudahBaca(id):
    try:
        notif = Notifications.query.filter_by(id=id).first()
        notif.status = 1

        db.session.commit()

        return response.ok('', 'Successfully change status!')

    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def update(id):
    try:
        title = request.json['title']
        description = request.json['description']

        notif = Notifications.query.filter_by(id=id).first()
        notif.title = title
        notif.description = description

        db.session.commit()

        return response.ok('', 'Successfully update data!')

    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def delete(id):
    try:
        notif = Notifications.query.filter_by(id=id).first()
        if not notif:
            return response.badRequest([], 'Empty....')

        db.session.delete(notif)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")