from app.main.models.SampleModel import ParentModel_1, ChildModel_1, ParentModel_2, ChildModel_2, ParentModel_3, ChildModel_3, ParentModel_4, ChildModel_4
from app.main import db
import uuid
import json

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def save_parent_1(data):
    new_parent = ParentModel_1(
        name=data['name']
    )
    save_changes(new_parent)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 200

def get_raw_data():
    data_raw = db.engine.execute('SELECT * FROM parent_1')
    names = [list(row) for row in data_raw]
    resp = {'data': names}
    return resp

def save_child_1(data):
    new_parent = ParentModel_1(
        id=str(uuid.uuid4()),
        name=data['name']
    )
    save_changes(new_user)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 200

def save_parent_4(data):
    new_parent = ParentModel_4(
        name=data['name']
    )
    save_changes(new_parent)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 200

def save_child_4(data):
    new_child = ChildModel_4(
    )
    save_changes(new_child)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 200
