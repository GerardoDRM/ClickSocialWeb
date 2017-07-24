from clicksocial import app, api, mongo, babel, admin
from flask_restful import Resource, reqparse
from flask import jsonify, request, session
from flask_cors import cross_origin
from bson.objectid import ObjectId
from bson.regex import Regex
import re
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView
from datetime import datetime

app.config['MONGODB_SETTINGS'] = {'DB': 'clicksocial'}

# Create models
db = MongoEngine()
db.init_app(app)


def create_dic(cursor):
    k = []
    for doc in cursor:
        k.append({key: (str(value) if key == "_id" else value)
                  for key, value in doc.items()})
    return k


@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return session.get('lang', 'es')

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
        else:
            convocation = mongo.db.convocation.find_one({"_id": ObjectId(id)}, {"_id":0})
            return jsonify(convocation)

        return jsonify(convocations=c)

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
                type_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.type.split(',') if len(i) > 2]
                for t in type_list:
                    t.flags ^= re.UNICODE
                group_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.group.split(',') if len(i) > 2]
                for g in group_list:
                    g.flags ^= re.UNICODE
                issue_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.issue.split(',') if len(i) > 2]
                for i in issue_list:
                    i.flags ^= re.UNICODE

                s = create_dic(mongo.db.organizations.find({
                    "$or": [
                        {"social_group": {"$in": group_list}},
                        {"type": {"$in": type_list}},
                        {"geo_issue": {"$in": issue_list}}
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



'''
    Get all organization stored on the database
    this class just retrieve all data without any constraint
    just on mobile
'''


class OrganizationMobile(Resource):

    @cross_origin()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('group', type=str, required=False)
        parser.add_argument('type', type=str, required=False)
        parser.add_argument('issue', type=str, required=False)
        parser.add_argument('filters', type=int, required=True)
        parser.add_argument('page', type=int, required=True)

        args = parser.parse_args()

        # Check filters
        if args.filters is 1: # Add filters
            # Check which filter to apply
            type_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.type.split(',') if len(i) > 2]
            for t in type_list:
                t.flags ^= re.UNICODE
            group_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.group.split(',') if len(i) > 2]
            for g in group_list:
                g.flags ^= re.UNICODE
            issue_list = [Regex.from_native(re.compile(str(i).replace("\"", "")+'.*')) for i in args.issue.split(',') if len(i) > 2]
            for i in issue_list:
                i.flags ^= re.UNICODE

            s = create_dic(mongo.db.organizations.find({
                "$or": [
                    {"social_group": {"$in": group_list}},
                    {"type": {"$in": type_list}},
                    {"geo_issue": {"$in": issue_list}}
                ]
            }).skip(args.page * 25).limit(25))
        else:
            s = create_dic(mongo.db.organizations.find({}).skip(args.page * 25).limit(25))

        return jsonify(organizations=s)

'''
    Get all data from directory stored on the database
    this class just retrieve all data without any constraint
'''


class DirectoryMobile(Resource):

    @cross_origin()
    def get(self):
        s = create_dic(mongo.db.directory.find({}).skip(args.page * 25).limit(25))
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
api.add_resource(OrganizationMobile,
                 '/api/v0/organizations_mobile',
                 endpoint="organizations_mobile")
api.add_resource(Directory,
                 '/api/v0/directory',
                 endpoint="directory")
api.add_resource(DirectoryMobile,
                 '/api/v0/directory_mobile',
                 endpoint="directory_mobile")


# Admin views
# Define mongoengine documents
class Convocation(db.Document):
    title = db.StringField(max_length=255)
    type = db.StringField(max_length=5)
    description = db.StringField(max_length=255)
    img = db.StringField(max_length=355)
    web = db.StringField(max_length=255)
    creation_date = db.DateTimeField(default=datetime.now)
    addresses = db.ListField(db.DictField())
    authors = db.ListField(db.DictField())
    model = db.ListField(db.StringField(max_length=255))


    def __unicode__(self):
        return self.title


class Author(db.EmbeddedDocument):
    name = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255)

class Address(db.EmbeddedDocument):
    state = db.StringField(max_length=255, required=True)
    city = db.StringField(max_length=255)

class Challenges(db.Document):
    title = db.StringField(max_length=255)
    model = db.ListField(db.StringField(max_length=255))
    creation_date = db.DateTimeField(default=datetime.now)
    description = db.StringField(max_length=255)
    challenge = db.StringField(max_length=255)
    img = db.StringField(max_length=355)
    comments = db.ListField(db.DictField())
    authors = db.ListField(db.EmbeddedDocumentField(Author))
    address = db.ListField(db.EmbeddedDocumentField(Address))
    likes = db.IntField()
    participants = db.IntField()


    def __unicode__(self):
        return self.title


class success_stories(db.Document):
    creation_date = db.DateTimeField(default=datetime.now)
    description = db.StringField(max_length=255)
    img = db.StringField(max_length=355)
    title = db.StringField(max_length=255)
    videos = db.ListField(db.StringField(max_length=255))


    def __unicode__(self):
        return self.title

class organizations(db.Document):
    model = db.StringField(max_length=255)
    entity = db.StringField(max_length=255)
    social_group = db.StringField(max_length=255)
    federal_entity = db.StringField(max_length=255)
    geo_issue = db.StringField(max_length=255)
    web = db.StringField(max_length=255)
    contact = db.StringField(max_length=255)
    email = db.StringField(max_length=255)
    type = db.StringField(max_length=255)

    def __unicode__(self):
        return self.entity

class directory(db.Document):
    social_reason = db.StringField(max_length=255)
    figure = db.StringField(max_length=255)
    representants = db.StringField(max_length=255)
    emails = db.StringField(max_length=255)
    federal_entity = db.StringField(max_length=255)
    place = db.StringField(max_length=255)
    street = db.StringField(max_length=255)
    network = db.StringField(max_length=255)

    def __unicode__(self):
        return self.figure


# Customized admin views
class ChallengesView(ModelView):
    column_filters = ['title']
    column_labels = dict(title='Titulo', model='Modelo', description='Descripcion', challenge='Reto', img='URL imagen')

    column_exclude_list = ['creation_date', 'comments', 'likes', 'participants', 'address', 'authors' ]
    form_excluded_columns = ['creation_date', 'comments', 'likes', 'participants', ]

    form_args = {
        'title': {
            'label': 'Titulo',
        },
        'model': {
            'label': 'Modelo',
        },
        'description': {
            'label': 'Descripcion',
        },
        'challenge': {
            'label': 'Reto',
        },
        'img': {
            'label': 'URL de imagen',
        },
        'authors': {
            'label': 'Autores',
        },
        'address': {
            'label': 'Direcciones',
        },

    }

class ConvocationView(ModelView):
    column_filters = ['title']
    column_labels = dict(title='Titulo', model='Modelo', description='Descripcion', web='Sitio web', img='URL imagen')

    column_exclude_list = ['creation_date', 'type', 'address', 'authors' ]
    form_excluded_columns = ['creation_date', 'type', ]

    form_args = {
        'title': {
            'label': 'Titulo',
        },
        'model': {
            'label': 'Modelo',
        },
        'description': {
            'label': 'Descripcion',
        },
        'web': {
            'label': 'URL de sitio web',
        },
        'img': {
            'label': 'URL de imagen',
        },
        'authors': {
            'label': 'Autores',
        },
        'address': {
            'label': 'Direcciones',
        },

    }


class SuccessStoriesView(ModelView):
    column_filters = ['title']
    column_labels = dict(title='Titulo', videos='Videos', description='Descripcion', img='URL imagen')

    column_exclude_list = ['creation_date',]
    form_excluded_columns = ['creation_date',]

    form_args = {
        'title': {
            'label': 'Titulo',
        },
        'videos': {
            'label': 'URL de videos',
        },
        'description': {
            'label': 'Descripcion',
        },
        'img': {
            'label': 'URL de imagen',
        },
    }

class DirectoryView(ModelView):
    column_filters = ['social_reason']
    column_labels = dict(social_reason='Razon Social', federal_entity='Entidad Federativa', figure='Figura',)

    column_exclude_list = ['representants', 'emails', 'place', 'street', 'network', ]

    form_args = {
        'social_reason': {
            'label': 'Razon Social',
        },
        'figure': {
            'label': 'Figura',
        },
        'representants': {
            'label': 'Representantes',
        },
        'emails': {
            'label': 'Emails',
        },
        'federal_entity': {
            'label': 'Entidad Federativa',
        },
        'place': {
            'label': 'Ubicacion',
        },
        'street': {
            'label': 'Calle',
        },
        'network': {
            'label': 'Red',
        },

    }

class OrganizationView(ModelView):
    column_filters = ['entity']
    column_labels = dict(model='Modelo', entity='Entidad', social_group='Grupo Social', federal_entity='Entidad Federativa',)

    column_exclude_list = ['geo_issue', 'web', 'contact', 'email', 'type', ]

    form_args = {
        'model': {
            'label': 'Modelo',
        },
        'entity': {
            'label': 'Entidad',
        },
        'social_group': {
            'label': 'Grupo Social',
        },
        'federal_entity': {
            'label': 'Entidad Federativa',
        },
        'geo_issue': {
            'label': 'Ubicacion',
        },
        'web': {
            'label': 'Sitio web',
        },
        'contact': {
            'label': 'Contacto',
        },
        'email': {
            'label': 'Email',
        },
        'type': {
            'label': 'Tipo',
        },

    }
admin.add_view(ConvocationView(Convocation))
admin.add_view(ChallengesView(Challenges))
admin.add_view(SuccessStoriesView(success_stories))
admin.add_view(DirectoryView(directory))
admin.add_view(OrganizationView(organizations))
