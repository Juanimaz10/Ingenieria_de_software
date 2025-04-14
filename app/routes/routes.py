class Route():

    def init_app(self, app):
        from app.controllers import article_bp

        app.register_blueprint(article_bp, url_prefix='/api/v1')
