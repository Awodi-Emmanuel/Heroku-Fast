from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql+psycopg2://emmycoder:Icon123_@localhost/junkdbasejunkdbase'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
    
    
# MODELS SECTIONS 

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    pet_type = db.Column(db.String(100), nullable=False)
    pet_age = db.Column(db.Integer(), nullable=False)
    pet_discreption = db.Column(db.String(100), nullable=False)
    
    
    def __repr__(self):
        return "<Pet %r>" % self.pet_name
    
    
    # Flask Simple route 
@app.route('/')
def index():
    return jsonify({"message":"Welcome to my first flask show"})
