from app.model.help import Helps
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import *

@jwt_required
def index():
    try:
        helps = Helps.query.all()
        data = transform(helps)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        return response.ok([], "Data kosong")

def transform(helps):
    array = []
    for i in helps:
        array.append(singleTransform(i))
    return array

def singleTransform(helps):
    data = {
        'id' : helps.id,
        'title' : helps.title,
        'description' : helps.description,
        'tanggal_notif' : helps.updated_at.strftime('%Y-%m-%d')
    }

    return data

def store():
    try:
        title = request.json['title']
        description = request.json['description']

        helps = Helps(title=title, description=description)
        db.session.add(helps)
        db.session.commit()

        return response.ok('', 'Successfully create data!')

    except Exception as e:
        print(e)
        return response.serverErrRequest([], 'Data failed to be processed')
        # return response.ok([], "Data kosong")

def update(id):
    try:
        title = request.json['title']
        description = request.json['description']

        helpvar = Helps.query.filter_by(id=id).first()
        helpvar.title = title
        helpvar.description = description

        db.session.commit()

        return response.ok('', 'Successfully update data!')

    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def delete(id):
    try:
        help = Helps.query.filter_by(id=id).first()
        if not help:
            return response.badRequest([], 'Empty....')

        db.session.delete(help)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")