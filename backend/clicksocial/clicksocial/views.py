from clicksocial.clicksocial import app, api, mongo
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_cors import cross_origin


def create_dic(cursor):
    k = []
    for doc in cursor:
        k.append({key: (str(value) if key == "_id" else value)
                  for key, value in doc.items()})
    return k


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}

'''
    Get all convocations stored on the database
    this class just retrieve all data without any constraint
'''


class Convocations(Resource):
    @cross_origin()
    def get(self):
        c = create_dic(mongo.db.convocation.find())
        test = [
            {
                "_id": "58f4f269516ea6d697a45bc8",
                "addresses": [
                    {
                        "city": "Puebla",
                        "state": "Puebla",
                        "street": "Calle 2"
                    }
                ],
                "authors": [
                    {
                        "email": "",
                        "name": "Coparmex"
                    }
                ],
                "creation_date": 122202.0,
                "description": "Lorem Ipsum",
                "img": "https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg",
                "model": [
                    "Pobreza",
                    "Sustentabilidad"
                ],
                "title": "Convocatoria",
                "type": "Municipal",
                "web": "www.google.com"
            }
        ]
        return jsonify(convocations=test)

'''
    Get all stories stored on the database
    this class just retrieve all data without any constraint
'''


class Stories(Resource):
    @cross_origin()
    def get(self):
        s = create_dic(mongo.db.success_stories.find(
            {}, {"creation_date": 1, "description": 1, "img": 1, "title": 1}))
        test = [
            {
                "_id": "58f4f2fa516ea6d697a45bc9",
                "creation_date": 122202.0,
                "description": "Lorem Ipsum",
                "img": "/img",
                "title": "Click Social"
            }
        ]
        return jsonify(stories=s)

'''
    Get all challenges stored on the database
    this class just retrieve all data without any constraint
'''


class Challenge(Resource):
    @cross_origin()
    def get(self):
        s = create_dic(mongo.db.challenges.find(
            {}, {"creation_date": 1, "description": 1, "img": 1, "title": 1, "likes":1}))
        test = [
            {
                "_id": "58f4f2fa516ea6d697a45bc9",
                "creation_date": 122202.0,
                "description": "Lorem Ipsum",
                "img": "/img",
                "title": "Click Social",
                "likes": 10
            }
        ]
        return jsonify(stories=s)

api.add_resource(HelloWorld, '/')
api.add_resource(Convocations, '/api/v0/convocations')
api.add_resource(Stories, '/api/v0/stories')
api.add_resource(Challenge, '/api/v0/challenges')
