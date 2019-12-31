from flask import request
from flask_restful import Resource
from ..services.sample_service import save_parent_1, get_raw_data, save_parent_4, save_child_4
import requests

class OneToMany(Resource):
    
    @classmethod
    def get(cls):
        data = get_raw_data()
        print(data)
        return data

    @classmethod
    def post(cls):
        data = request.get_json()
        parent_data = dict(name=data['name'])
        return save_parent_1(data=parent_data)


class ManyToMany(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        parent_data = dict(name=data['name'])
        return save_parent_4(data=parent_data)

class ManyToManyChild(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        parent_data = dict()
        return save_child_4(data=parent_data)