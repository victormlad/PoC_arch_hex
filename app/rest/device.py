from flask import Blueprint, jsonify, request

from app import api

device_blueprint = Blueprint('device', __name__)
api = api.Api()


@device_blueprint.route('/all')
def get_all_devices():
    return jsonify(api.get_all_devices())


@device_blueprint.route('/<int:device_id>')
def get_devices(device_id):
    return jsonify(api.get_device(device_id))


@device_blueprint.route('/create', methods=['POST'])
def create_device():
    data = request.json
    id = data.get('id')
    type = data.get('type', None)
    subtype = data.get('subtype', None)
    return jsonify(api.create_device(id, type, subtype))


@device_blueprint.route('/update/<int:device_id>')
def update_device(device_id):
    data = request.json
    changes = data.get('changes')
    return jsonify(api.device_update(device_id, changes))
