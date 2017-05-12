from clicksocial import app, api, mongo
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_cors import cross_origin
from bson.objectid import ObjectId
from bson.regex import Regex
import re

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
                    "description": '''
                        Programa dirigido a empresas legalmente establecidas que generen productos, servicios
                        y/o modelos de negocio innovadores con un alto impacto social y económico, que además
                        contribuyan positivamente al medio ambiente, generen beneficios para su comunidad y
                        tengan potencial para volverse global.
                        La convocatoria 3.3 “Impulso a Emprendimientos de Alto Impacto” del Fondo Nacional
                        Emprendedor, busca apoyar emprendimientos de alto impacto que cuenten con alto
                        potencial económico, basados en nuevas y/o mejores soluciones que se traduzcan en
                        productos, servicios y/o modelos de negocio con un impacto integral en su entorno y que
                        requieran herramientas para fortalecer su operación, generar valor agregado y maximizar
                        su crecimiento.
                        No importa si te acabas de constituir (startup) o ya estás creciendo (scaleup), si requieres
                        de acompañamiento y asesoría especializada para poder generar valor en tu negocio y
                        crecer, esta convocatoria te brinda la oportunidad de acercarte a los expertos, adquirir e
                        implementar tecnología y maquinaria para eficientar procesos de innovación y obtener
                        validaciones nacionales e internacionales que faciliten tu operación y posicionamiento en
                        el mercado.
                    ''',
                    "img": "http://s3-us-west-2.amazonaws.com/puntoapunto.com.ar/wp-content/uploads/2017/02/07103647/startups-696x450-696x450.jpg",
                    "model": [
                        "Pobreza",
                        "Sustentabilidad"
                    ],
                    "title": "Convocatoria para Emprendimiento de alto impacto",
                    "type": "Municipal",
                    "web": "www.inadem.mx"
                },
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
                    "description": '''
                                        Programa dirigido a empresas legalmente establecidas que generen productos, servicios
                                        y/o modelos de negocio innovadores con un alto impacto social y económico, que además
                                        contribuyan positivamente al medio ambiente, generen beneficios para su comunidad y
                                        tengan potencial para volverse global.
                                        La convocatoria 3.3 “Impulso a Emprendimientos de Alto Impacto” del Fondo Nacional
                                        Emprendedor, busca apoyar emprendimientos de alto impacto que cuenten con alto
                                        potencial económico, basados en nuevas y/o mejores soluciones que se traduzcan en
                                        productos, servicios y/o modelos de negocio con un impacto integral en su entorno y que
                                        requieran herramientas para fortalecer su operación, generar valor agregado y maximizar
                                        su crecimiento.
                                        No importa si te acabas de constituir (startup) o ya estás creciendo (scaleup), si requieres
                                        de acompañamiento y asesoría especializada para poder generar valor en tu negocio y
                                        crecer, esta convocatoria te brinda la oportunidad de acercarte a los expertos, adquirir e
                                        implementar tecnología y maquinaria para eficientar procesos de innovación y obtener
                                        validaciones nacionales e internacionales que faciliten tu operación y posicionamiento en
                                        el mercado.
                                    ''',
                    "img": "https://assets.entrepreneur.com/content/16x9/822/20161027155704-Depositphotos-126342088-l-2015.jpeg",
                    "model": [
                        "Pobreza",
                        "Sustentabilidad"
                    ],
                    "title": "Alto Impacto Coparmex",
                    "type": "Municipal",
                    "web": "www.inadem.mx"
                }
            ]
        else:
            convocation = mongo.db.convocation.find_one({"_id": ObjectId(id)}, {"_id":0})
            return jsonify(convocation)

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
        else:
            story = mongo.db.success_stories.find_one({"_id": ObjectId(id)}, {"_id":0})
            return jsonify(story)

        return jsonify(stories=s)

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
        else:
            challenge = mongo.db.challenges.find_one({"_id": ObjectId(id)}, {"_id":0})
            return jsonify(challenge)

        return jsonify(challenges=s)

'''
    This class inserts and gets comments on specific challenge
'''
class Comments(Resource):

    @cross_origin()
    def get(self, id):
        challenge = mongo.db.challenges.find_one({"_id": ObjectId(id)}, {"comments":1})
        return jsonify(challenge)

    @cross_origin()
    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('comment', type=dict, required=True)
        args = parser.parse_args()

        result = mongo.db.challenge.update_one({"_id":ObjectId(id)}, {"$push": args.comment})
        message = {
            "status": 500
        }
        if result.matched_count is 1:
            message["status"] = 200

        return jsonify(message)


'''
    Get all challenges stored on the database
    this class just retrieve all data without any constraint
'''


class Organization(Resource):

    @cross_origin()
    def get(self, id=None):

        if id is None:
            parser = reqparse.RequestParser()
            parser.add_argument('group', type=str, required=False)
            parser.add_argument('type', type=str, required=False)
            parser.add_argument('issue', type=str, required=False)
            parser.add_argument('filters', type=int, required=True)
            args = parser.parse_args()

            # Check filters
            if args.filters is 1: # Add filters
                # Check which filter to apply
                type_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.type.split(',')]
                for t in type_list:
                    t.flags ^= re.UNICODE
                group_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.group.split(',')]
                for g in group_list:
                    g.flags ^= re.UNICODE
                issue_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.issue.split(',')]
                for i in issue_list:
                    i.flags ^= re.UNICODE

                s = create_dic(mongo.db.organizations.find({
                    "$or": [
                        {"social_group": {"$in": group_list}},
                        {"type": {"$in": type_list}},
                        {"issue": {"$in": issue_list}}
                    ]
                }))
            else:
                s = create_dic(mongo.db.organizations.find({}))
        else:
            organization = mongo.db.organizations.find_one(
                {"_id": ObjectId(id)}, {"_id": 0})
            return jsonify(organization)
        return jsonify(organizations=s)

'''
    Get all data from directory stored on the database
    this class just retrieve all data without any constraint
'''


class Directory(Resource):

    @cross_origin()
    def get(self):
        s = create_dic(mongo.db.directory.find({}))
        return jsonify(directory=s)

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
api.add_resource(Directory,
                 '/api/v0/directory',
                 endpoint="directory")
