from flask import request
from flask_restful import Resource
from ..services.sample_service import save_parent_1
import requests

class OneToMany(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        parent_data = dict(name=data['name'])
        return save_parent_1(data=parent_data)


class ManyToOne(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        parent_data = dict(name=data['name'])
        return save_parent_1(data=parent_data)