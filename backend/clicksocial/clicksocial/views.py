from clicksocial.clicksocial import app, api, mongo
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_cors import cross_origin
from bson.objectid import ObjectId


def create_dic(cursor):
    k = []
    for doc in cursor:
        k.append({key: (str(value) if key == "_id" else value)
                  for key, value in doc.items()})
    return k


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'lucas'}

'''
    Get all convocations stored on the database
    this class just retrieve all data without any constraint
'''


class Convocations(Resource):

    @cross_origin()
    def get(self, id=None):
        if id is None:
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
                    "creation_date": 1492659697,
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
        else:
            convocation = mongo.db.convocation.find_one({"_id": ObjectId(id)})
            test = {
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
                "creation_date": 1492659697,
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
            return jsonify(test)

        return jsonify(convocations=test)

'''
    Get all stories stored on the database
    this class just retrieve all data without any constraint
'''


class Stories(Resource):

    @cross_origin()
    def get(self, id=None):
        if id is None:
            s = create_dic(mongo.db.success_stories.find(
                {}, {"creation_date": 1, "description": 1, "img": 1, "title": 1}))
            test = [
                {
                    "_id": "58f4f2fa516ea6d697a45bc9",
                    "creation_date": 1492659697,
                    "description": "Lorem Ipsum",
                    "img": "https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg",
                    "title": "Click Social"
                }
            ]
        else:
            story = mongo.db.success_stories.find_one({"_id": ObjectId(id)})
            test = {
                "_id": "58f4f2fa516ea6d697a45bc9",
                "creation_date": 1492659697,
                "description": "Lorem Ipsum",
                "img": "https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg",
                "title": "Click Social"
            }
            return jsonify(test)

        return jsonify(stories=test)

'''
    Get all challenges stored on the database
    this class just retrieve all data without any constraint
'''


class Challenge(Resource):

    @cross_origin()
    def get(self, id=None):
        if id is None:
            s = create_dic(mongo.db.challenges.find(
                {}, {"creation_date": 1, "description": 1, "img": 1, "title": 1, "likes": 1}))
            test = [
                {
                    "_id": "58f4f2fa516ea6d697a45bc9",
                    "creation_date": 1492659697,
                    "description": "Lorem Ipsum",
                    "img": "https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg",
                    "title": "Click Social",
                    "likes": 10
                },
                {
                    "_id": "58f4f2fa516ea6d697a45bc9",
                    "creation_date": 1492659697,
                    "description": "Lorem Ipsum",
                    "img": "https://i.ytimg.com/vi/opKg3fyqWt4/hqdefault.jpg",
                    "title": "Click Social",
                    "likes": 10
                }
            ]
        else:
            challenge = mongo.db.challenges.find_one({"_id": ObjectId(id)})
            test = {
                "_id": "58f4f144516ea6d697a45bc7",
                "title": "Reto 1",
                "model": [
                    "Pobreza",
                    "Sustentabilidad"
                ],
                "creation_date": 1492659697,
                "description": "Lorem Ipsum",
                "challenge": "Lorem Ipsum",
                "img": "/img",
                "comments": [
                    {
                        "user": "0124",
                        "name": "Test",
                        "content": "test",
                        "publish_date": 1492659697
                    }
                ],
                "authors": [
                    {
                        "name": "Gerar de la Rosa",
                        "email": "contacto.craftcode@gmail.com"
                    }
                ],
                "likes": 10,
                "participants": 20,
                "address": [
                    {
                        "state": "Puebla",
                        "city": "Puebla"
                    }
                ]
            }
            return jsonify(test)
        return jsonify(challenges=test)

'''
    Get all challenges stored on the database
    this class just retrieve all data without any constraint
'''


class Organization(Resource):

    @cross_origin()
    def get(self, id=None):
        if id is None:
            s = create_dic(mongo.db.organizations.find({}))
            test = [
                {
                    "_id": "58f4efe9516ea6d697a45bc6",
                    "model": "Fundacion Empresarial",
                    "entity": "American Express, S.A. de C.V",
                    "social_group": "Poblacion en general",
                    "federal_entity": "Ciudad de Mexico",
                    "geo_issue": "Nacional",
                    "web": "www.americanexpress.com",
                    "contact": [
                        "Adriana Rivera, Directora de Asuntos Corporativos y Comunicacion"
                    ],
                    "email": "adriana.a.rivera@aexp.com",
                    "type": "Desarrollo Integral"
                }
            ]
        else:
            organization = mongo.db.organization.find_one(
                {"_id": ObjectId(id)})
            test = {
                "_id": "58f4efe9516ea6d697a45bc6",
                "model": "Fundacion Empresarial",
                "entity": "American Express, S.A. de C.V",
                "social_group": "Poblacion en general",
                "federal_entity": "Ciudad de Mexico",
                "geo_issue": "Nacional",
                "web": "www.americanexpress.com",
                "contact": [
                    "Adriana Rivera, Directora de Asuntos Corporativos y Comunicacion"
                ],
                "email": "adriana.a.rivera@aexp.com",
                "type": "Desarrollo Integral"
            }
            return jsonify(test)
        return jsonify(organizations=test)


api.add_resource(HelloWorld, '/')
api.add_resource(Convocations,
                 '/api/v0/convocations',
                 '/api/v0/convocations/<id>',
                 endpoint="convocations")
api.add_resource(Stories,
                 '/api/v0/stories',
                 '/api/v0/stories/<id>',
                 endpoint="stories")
api.add_resource(Challenge,
                 '/api/v0/challenges',
                 '/api/v0/challenges/<id>',
                 endpoint="challenges")
api.add_resource(Organization,
                 '/api/v0/organizations',
                 '/api/v0/organizations/<id>',
                 endpoint="organizations")
