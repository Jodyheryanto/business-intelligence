from app.model.word_cloud import Word_Clouds
from app.model.post import Posts
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import *

@jwt_required
def printData(user_id):
    try:
        word_clouds = Word_Clouds.query.filter(Word_Clouds.user_id==user_id).all()
        # Word_Clouds.query.filter(Word_Clouds.aplikasi==aplikasi).all()
        data = transform(word_clouds)
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def transform(word_clouds):
    array = []
    for i in word_clouds:
        array.append(singleTransform(i))
    return array

def singleTransform(word_clouds):
    data = {
        'id' : word_clouds.id,
        'word' : word_clouds.word,
        'count' : word_clouds.value,
        'sentiment' : word_clouds.sentiment,
        'link_review' : word_clouds.sample_id,
        'sumber': word_clouds.posts.sources.name
    }

    return data