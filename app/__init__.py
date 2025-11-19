from flask import Flask    
def create_app():
    app = Flask("_name_")
    # Config can go here (e.g., app.config["DEBUG"] = True)
    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")
    return app
