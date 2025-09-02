from flask_jwt_extended import JWTManager, create_access_token

def init_auth(app):
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    JWTManager(app)

def login_user(username, password):
    if username == "user" and password == "pass":
        return create_access_token(identity=username)
    return None
