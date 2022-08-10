from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql+psycopg2://emmycoder:Icon123_@localhost/junkdbasejunkdbase'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
    
    
# MODELS SECTIONS 

class Pet(db.Model):
    __tablename__ = 'pets'