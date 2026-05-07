from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    return jsonify({
        "username": username,
        "password": password,
        "message": "登录"
    })

@user_bp.route('/logout', methods=['GET'])
def logout():
    return jsonify({
        "message": "登出"
    })

@user_bp.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    new_password = data.get('new_password')
    return jsonify({
        "username": username,
        "old_password": password,
        "new_password": new_password,
        "message": "修改密码"
    })

@user_bp.route('/change-username', methods=['POST'])
def change_username():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    new_username = data.get('new_username')
    return jsonify({
        "username": username,
        "password": password,
        "new_username": new_username,
        "message": "修改用户名"
    })