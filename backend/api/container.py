from calendar import month

from flask import Blueprint, jsonify, request

container_bp = Blueprint('container', __name__)

@container_bp.route('/container/<int:con_id>', methods=['GET'])
def get_container(con_id):
    return jsonify({
        "id": con_id,
        "message": "获取容器列表"
    })

@container_bp.route('/container-list', methods=['GET'])
def get_container_list():
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 12, type=int)
    return jsonify({
        "page": page,
        "size": size,
        "message": "获取容器列表"
    })

@container_bp.route('/container', methods=['POST'])
def create_container():
    data = request.get_json()
    name = data.get('name')
    note = data.get('note')
    cfg_id = data.get('cfg_id')
    return jsonify({
        "name": name,
        "note": note,
        "cfg_id": cfg_id,
        "message": "创建容器"
    })

@container_bp.route('/container>', methods=['PUT'])
def update_container():
    data = request.get_json()
    con_id = data.get('con_id')
    name = data.get('name')
    note = data.get('note')
    cfg_id = data.get('cfg_id')
    return jsonify({
        "con_id": con_id,
        "name": name,
        "note": note,
        "cfg_id": cfg_id,
        "message": "更新容器"
    })

@container_bp.route('/container/<int:con_id>', methods=['DELETE'])
def delete_container(con_id):
    return jsonify({
        "con_id": con_id,
        "message": "删除容器"
    })
