from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from aplication.usuario.routes import auth
# Flask app creation
app = Flask(__name__)

# Ugly and confusing tangent of in-line config stuff
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = 'GDtfDCFYjD'
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:jos84mar19@localhost:3306/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = False  # actually I want debug to be off now

db = SQLAlchemy(app)

app.register_blueprint(auth)
db.create_all()


