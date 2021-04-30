"""Arquivo main da API"""
import firebase_admin
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS

from views.heroes import HeroesHandler, HeroHandler

cred = firebase_admin.credentials.Certificate(
    './tourofheroes2joao-firebase-adminsdk-kzu0e-8e16191172.json')

firebase_admin.initialize_app(credential=cred)

# Aqui iniciamos a API
app = Flask(__name__)
CORS(app)
API = Api(app)


@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothing at this URL.', 404


# Nossa classe principal
class Index(Resource):
    """ class return API index """

    def get(self):
        """return API"""
        return {"API": "Heroes"}


# Nossa primeira url
API.add_resource(Index, '/', endpoint='index')
API.add_resource(HeroesHandler, '/heroes', endpoint='heroes')
API.add_resource(HeroHandler, '/hero/<hero_id>', endpoint='hero')

if __name__ == '__main__':
    # Isso é utilizado somente para executar a aplicação local. Quando
    # realizarmos o deploy para o Google App Engine, o webserver deles ira
    # iniciar a aplicação de outra forma
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]