from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from .config import Config

# app = Flask(__name__)
# #CSRF TOKEN CONFIGURATION
# app.config['SECRET_KEY']='7cde99c7757343b964dfab8a36739d7f'
# #DATABASE configuration
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'   ##using sqlite inbuilt database for development purpose

db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'
mail=Mail()
 #Mail Configuration
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] =os.environ.get('MAIL_PASSWORD')

# from flaskblog import routes

def create_app(default=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app



