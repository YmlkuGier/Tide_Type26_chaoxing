from flask import Flask, jsonify
from backend.api.container import container_bp
from backend.api.configuration import configuration_bp
from backend.api.user import user_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(container_bp)
app.register_blueprint(configuration_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
