# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/home')
# def hello_world():
#     return '<h1>Hello, Bebo!</h1>'
#
# @app.route('/about')
# def about():
#     return '<h1> About Page Information</h1>'
#
# if __name__=='__main__':
#     app.run(debug=True)

########################################################################################################################

from flaskblog import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)