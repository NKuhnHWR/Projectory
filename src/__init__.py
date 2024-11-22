from flask import Flask

def create_app():
    """App factory function."""
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    # Register blueprints
    from src.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
