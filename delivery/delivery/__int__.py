from .main import bp

def init_APP(app):
    app.register_blueprint(bp)