#!/usr/bin/python3
""" Nameless Module for Task 6 """

from flask import Flask
from flask_restx import Resource, Api, fields

app = Flask(__name__)
api = Api(app, version='0.5', title='Dungeon API', description='API used for creating and updating of dungeons')

ns = api.namespace('dungeon', description='Everything about your dungeons')

# declared but not used in the code below. This is supposed to be used in 'marshaling'
dungeon = api.model('Dungeon', {
    'id': fields.Integer(readonly=True, description='The unique id for the dungeon'),
    'name': fields.String(required=True, description='The name of the dungeon')
})

@ns.route('/')
class Dungeon(Resource):
    """ endpoint handler Class """
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.dungeons = []

    @ns.doc('getDungeon')
    def get(self):
        """ Get dungeon details """
        return {'method': 'get'}

    @ns.doc('updateDungeon')
    def put(self, index, data):
        """ Update and existing dungeon """
        self.dungeons[index].update(data)
        return {'method': 'put'}

    @ns.doc('addDungeon')
    def post(self, data):
        """ Add a new dungeon to the world """
        self.counter = self.counter + 1
        self.dungeons.append(data)
        return {'method': 'post'}


# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
