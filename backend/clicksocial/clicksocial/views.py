from clicksocial import app, api, mongo
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
                    "description": '''
                        Busca formar líderes con valores en procesos democráticos para incidir en lo nacional con
                        participación ciudadana desde lo local (escuela, colonia, municipio).
                        De manera que los jóvenes puedan vivir los procesos que conforman la Democracia
                        para comprenderlos en un espacio micro y mostrándoles que pueden participar resolviendo
                        problemas juntos.
                        Está dirigido hacia jóvenes entre 15 y 18 años ya que son aquellos que se encuentran muy
                        cercanos a participar en los procesos democráticos aunque se puede trabajar con otros sectores
                        además de que puede ser adaptable a Educación Formal Escuelas Y Educación No Formal
                        (unidades habitacionales y comunidades indígenas.
                    ''',
                    "img": "https://media.licdn.com/media/p/2/000/2bd/1d5/249157f.png",
                    "title": "Código Ciudadania"
                },
                {
                    "_id": "58f4f2fa516ea6d697a45bc9",
                    "creation_date": 1492659697,
                    "description": '''
                        Sociedad en Movimiento, A.C. es una organización
                        de la sociedad civil de naturaleza apartidista y sin fines
                        de lucro que busca –entre otros objetivos–, promover,
                        fomentar y articular la participación ciudadana en la
                        vida social, educativa y cultural de México.
                        En cumplimiento de sus objetivos, en los años
                        recientes, Sociedad en Movimiento ha desarrollado una
                        propuesta didáctica que denomina Democracia del
                        Futuro, con base en un enfoque educativo que facilita
                        la solución de retos mediante el diálogo, la creación de
                        propuestas y la toma de decisiones grupales.
                    ''',
                    "img": "http://www.movilidad.enmovimientorevista.com/wp-content/uploads/2014/04/peatones.jpg",
                    "title": "Talleres breves para la formación ciudadana"
                }
            ]
        else:
            story = mongo.db.success_stories.find_one({"_id": ObjectId(id)})
            test = {
                "_id": "58f4f2fa516ea6d697a45bc9",
                "creation_date": 1492659697,
                "description": '''
                    Busca formar líderes con valores en procesos democráticos para incidir en lo nacional con
                    participación ciudadana desde lo local (escuela, colonia, municipio).
                    De manera que los jóvenes puedan vivir los procesos que conforman la Democracia
                    para comprenderlos en un espacio micro y mostrándoles que pueden participar resolviendo
                    problemas juntos.
                    Está dirigido hacia jóvenes entre 15 y 18 años ya que son aquellos que se encuentran muy
                    cercanos a participar en los procesos democráticos aunque se puede trabajar con otros sectores
                    además de que puede ser adaptable a Educación Formal Escuelas Y Educación No Formal
                    (unidades habitacionales y comunidades indígenas.
                ''',
                "img": "https://media.licdn.com/media/p/2/000/2bd/1d5/249157f.png",
                "title": "Código Ciudadania"
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
                    "description": """
                        Transformar  Nuestro Mundo es el  lema de la Agenda 2030,
                        la nueva agenda internacional que desgrana los objetivos
                        de la comunidad internacional en el periodo 2016-2030 para
                        erradicar la pobreza y favorecer un desarrollo sostenible e igualitario.
                    """,
                    "img": "http://www.aecid.es/Centro-Documentacion/PublishingImages/Noticias/2015/09/V%C3%ADdeo%20Agenda%202030.png?RenditionID=8",
                    "title": "El reto de los ODS",
                    "likes": 10
                },
                {
                    "_id": "58f4f2fa516ea6d697a45bc9",
                    "creation_date": 1492659697,
                    "description": '''
                        A pesar de los avances de grandes industrias, de
                        pequeñas y medianas empresas innovando y demostrando
                        diferentes maneras de pensar, hacer y actuar,
                        hay grandes retos a corto, mediano y largo plazo que
                        se deben enfrentar para que una región tan compleja y
                        diversa como lo es Latinoamérica pueda ser referente
                        mundial en temas de sostenibilidad:
                    ''',
                    "img": "http://ep01.epimg.net/elpais/imagenes/2016/02/18/planeta_futuro/1455818338_104124_1455818881_noticia_normal_recorte1.jpg",
                    "title": "El reto de los ODS",
                    "likes": 10
                }
            ]
        else:
            challenge = mongo.db.challenges.find_one({"_id": ObjectId(id)})
            test = {
                "_id": "58f4f144516ea6d697a45bc7",
                "title": "El reto de los ODS",
                "model": [
                    "Pobreza",
                    "Sustentabilidad"
                ],
                "creation_date": 1492659697,
                "description": '''
                    A pesar de los avances de grandes industrias, de
                    pequeñas y medianas empresas innovando y demostrando
                    diferentes maneras de pensar, hacer y actuar,
                    hay grandes retos a corto, mediano y largo plazo que
                    se deben enfrentar para que una región tan compleja y
                    diversa como lo es Latinoamérica pueda ser referente
                    mundial en temas de sostenibilidad:
                ''',
                "challenge": '''
                    Se deben establecer sistemas de apoyo de apoyo gubernamental
                    y financiero para acompañar organizaciones que nunca han
                    hablado de sostenibilidad. Aún se conservan estilos
                    gerenciales basados en paradigmas sobre la importancia
                    estratégica de la sostenibilidad y con los cuales hay que
                    realizar un proceso de entendimiento para que se comprendan
                    que se pueden tener beneficios sociales, ambientales pero también económicos.
                    Innovadores y adaptadores tempranos lo hacen actualmente,
                    el reto es llegar a las mayorías tempranas y tardías,
                    empresas que aún no saben cómo establecer prácticas más sostenibles.
                 ''',
                "img": "http://ep01.epimg.net/elpais/imagenes/2016/02/18/planeta_futuro/1455818338_104124_1455818881_noticia_normal_recorte1.jpg",
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
                s = create_dic(mongo.db.organizations.find({
                    "$or": [
                        {"social_group": {"$in": args.group.split(',')}},
                        {"type": {"$in": args.type.split(',')}},
                        {"issue": {"$in": args.issue.split(',')}}
                    ]
                }))
            else:
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
                    "type": "Desarrollo Integral",
                    "img":"https://www.sams.com.mx/Images/Informativas/amex_1.jpg",
                    "description": "ok"
                },
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
                    "type": "Desarrollo Integral",
                    "img":"https://www.sams.com.mx/Images/Informativas/amex_1.jpg",
                    "description": "ok"
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
                "description": "ok",
                "geo_issue": "Nacional",
                "web": "www.americanexpress.com",
                "contact": [
                    "Adriana Rivera, Directora de Asuntos Corporativos y Comunicacion"
                ],
                "email": "adriana.a.rivera@aexp.com",
                "type": "Desarrollo Integral",
                "img":"https://www.sams.com.mx/Images/Informativas/amex_1.jpg"
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
