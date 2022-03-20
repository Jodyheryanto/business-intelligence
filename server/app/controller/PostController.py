from app.model.post import Posts
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import *


def transform(posts):
    array = []
    for i in posts:
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
            'user_name' : posts.username,
            'user_avatar' : posts.user_avatar,
            'post' : posts.post,
            'tanggal_post' : posts.tanggal_post.strftime('%Y-%m-%d'),
            'sumber' : posts.sources.name,
            'aplikasi' : posts.users.nama_aplikasi,
            'link_review' : posts.link_review,
            'rating' : posts.rating,
            'sentiment' : posts.sentiment
        }
        return response.ok(data, "")
    except Exception as e:
        # print(e)
        # return response.serverErrRequest([], 'Data failed to be processed')
        return response.ok([], "Data kosong")

def singleTransform(posts):
    data = {
        'id' : posts.id,
        'user_name' : posts.user_name,
        'user_avatar' : posts.user_avatar,
        'post' : posts.post,
        'tanggal_post' : posts.tanggal_post,
        'sumber' : posts.sources.name,
        'aplikasi' : posts.users.nama_aplikasi,
        'link_review' : posts.link_review,
        'rating' : posts.rating,
        'sentiment' : posts.sentiment
    }

    return data

def store():
    try:
        user_name = request.json['user_name']
        user_avatar = request.json['user_avatar']
        post = request.json['post']
        tanggal_post = request.json['tanggal_post']
        sumber = request.json['post']
        aplikasi = request.json['aplikasi']
        link_review = request.json['link_review']
        rating = request.json['rating']
        sentiment = request.json['sentiment']

        posts = Posts(user_name=user_name, user_avatar=user_avatar, post=post, tanggal_post=tanggal_post, sumber=sumber,
        aplikasi=aplikasi, link_review=link_review, rating=rating, sentiment=sentiment)
        db.session.add(posts)
        db.session.commit()

        return response.ok('', 'Successfully create data!')

    except Exception as e:
        print(e)

def update(id):
    try:
        user_name = request.json['user_name']
        user_avatar = request.json['user_avatar']
        post = request.json['post']
        tanggal_post = request.json['tanggal_post']
        sumber = request.json['sumber']
        aplikasi = request.json['aplikasi']
        link_review = request.json['link_review']
        rating = request.json['rating']
        sentiment = request.json['sentiment']

        post_val = Posts.query.filter_by(id=id).first()
        post_val.user_name = user_name
        post_val.user_avatar = user_avatar
        post_val.post = post
        post_val.tanggal_post = tanggal_post
        post_val.sumber = sumber
        post_val.aplikasi = aplikasi
        post_val.link_review = link_review
        post_val.rating = rating
        post_val.sentiment = sentiment

        db.session.commit()

        return response.ok('', 'Successfully update data!')

    except Exception as e:
        print(e)

def delete(id):
    try:
        post = Posts.query.filter_by(id=id).first()
        if not post:
            return response.badRequest([], 'Empty....')

        db.session.delete(post)
        db.session.commit()

        return response.ok('', 'Successfully delete data!')
    except Exception as e:
        print(e)