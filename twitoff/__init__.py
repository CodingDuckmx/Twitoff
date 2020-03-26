from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from twitoff.models import db, migrate
from twitoff.users.routes import users
from twitoff.tweets.routes import twitter_routes
from twitoff.main.routes import main
from twitoff.admin.routes import admin_routes


# app = Flask(__name__)
# app.config['SECRET_KEY'] = '8d96f77b72f3719a7df238f1e6347df0' #prevents cookies to be modified
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # db get created in the relative path

# db.init_app(app)
# migrate.init_app(app,db)

# from twitoff.users.routes import users
# from twitoff.tweets.routes import twitter_routes
# from twitoff.main.routes import main

# app.register_blueprint(users)
# app.register_blueprint(twitter_routes)
# app.register_blueprint(main)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8d96f77b72f3719a7df238f1e6347df0' #prevents cookies to be modified
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web_app_ls.db' # db get created in the relative path
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    app.register_blueprint(users)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(main)
    app.register_blueprint(admin_routes)

    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)


