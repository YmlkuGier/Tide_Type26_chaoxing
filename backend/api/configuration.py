from flask import Blueprint, jsonify, request

configuration_bp = Blueprint('configuration', __name__)

@configuration_bp.route('/configuration/<int:cfg_id>', methods=['GET'])
def get_configuration(cfg_id):
    return jsonify({
        "id": cfg_id,
        "message": "获取配置"
    })

@configuration_bp.route('/configuration-list', methods=['GET'])
def get_configuration_list():
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 12, type=int)
    return jsonify({
        "page": page,
        "size": size,
        "message": "获取配置列表"
    })

@configuration_bp.route('/configuration', methods=['POST'])
def create_configuration():
    data = request.get_json()
    name = data.get('name')
    note = data.get('note')
    cfg = data.get('cfg')
    return jsonify({
        "name": name,
        "note": note,
        "cfg": cfg,
        "message": "创建配置"
    })

@configuration_bp.route('/configuration', methods=['PUT'])
def update_configuration():
    data = request.get_json()
    cfg_id = data.get('cfg_id')
    name = data.get('name')
    note = data.get('note')
    cfg = data.get('cfg')
    return jsonify({
        "cfg_id": cfg_id,
        "name": name,
        "note": note,
        "cfg": cfg,
        "message": "更新配置"
    })

@configuration_bp.route('/configuration/<int:cfg_id>', methods=['DELETE'])
def delete_configuration(cfg_id):
    return jsonify({
        "cfg_id": cfg_id,
        "message": "删除配置"
    })