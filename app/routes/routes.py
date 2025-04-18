class Route():

    def init_app(self, app):
        from app.controllers import article_bp, brand_bp, category_bp

        app.register_blueprint(article_bp, url_prefix='/api/v1')
        app.register_blueprint(brand_bp, url_prefix='/api/v1')
        app.register_blueprint(category_bp, url_prefix='/api/v1')
