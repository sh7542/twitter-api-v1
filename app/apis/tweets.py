# app/apis/tweets.py
from flask_restplus import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

model = api.model('Model', {
    'text': fields.String,
    'id': fields.Integer,
    'created_at': fields.DateTime
})
@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class Tweet(Resource):
    @api.marshal_with(model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
