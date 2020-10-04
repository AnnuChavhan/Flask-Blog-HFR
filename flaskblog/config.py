import  os

class Config:
    #CSRF TOKEN CONFIGURATION
    SECRET_KEY='7cde99c7757343b964dfab8a36739d7f'
    #DATABASE configuration
    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'   ##using sqlite inbuilt database for development purpose
     #Mail Configuration
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')