from unittest import result
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, abort 
from flask_cors import CORS, cross_origin


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'postgresql+psycopg2://emmycoder:Icon123_@localhost/junkdbasejunkdbase'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


    
# MODELS SECTIONS 

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    pet_type = db.Column(db.String(100), nullable=False)
    pet_age = db.Column(db.Integer(), nullable=False)
    pet_description = db.Column(db.String(100), nullable=False)
    
    
    def __repr__(self):
        return "<Pet %r>" % self.pet_name
    
    
    # Flask Simple route 

@cross_origin()
@app.route('/')
def index():
    return jsonify({"message":"Welcome to my first flask show"})

@cross_origin()
@app.route('/pets', methods=['POST'])
def create_pet():
    pet_data = request.json
    
    pet_name = pet_data['pet_name']
    pet_type = pet_data['pet_type']
    pet_age = pet_data['pet_age']
    pet_description = pet_data['pet_description']
    
    pet_description = pet_data['pet_description']
    
    pet = Pet(pet_name=pet_name, pet_type=pet_type, pet_age=pet_age, pet_description=pet_description)
    db.session.add(pet)
    db.session.commit()
    
    return jsonify({"success": True, "response":"Pet added"})


@cross_origin()
@app.route('/getpets', methods = ['GET'])
def getpets():
     all_pets = []
     pets = Pet.query.all()
     print(type(pets))
     for pet in pets:
          results = {
                    "pet_id":pet.id,
                    "pet_name":pet.pet_name,
                    "pet_age":pet.pet_age,
                    "pet_type":pet.pet_type,
                    "pet_description":pet.pet_description, }
          all_pets.append(results)

     return jsonify(
            {
                "success": True,
                "pets": all_pets,
                "total_pets": len(pets),
            }
        )
        
@cross_origin()
@app.route("/pets/<int:pet_id>", methods = ["PATCH"])
def update_pet(pet_id):
    pet = Pet.query.get(pet_id)
    pet_age = request.json['pet_age']
    pet_description = request.json['pet_description']

    if pet is None:
        abort(404)
    else:
        pet.pet_age = pet_age
        pet.pet_description = pet_description
        db.session.add(pet)
        db.session.commit()
        return jsonify({"success": True, "response": "Pet Details updated"})
    
@cross_origin()
@app.route('/pet/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    pet_age = request.json['pet_age']
    pet_description = request.josn['pet_description']
    
    if pet is None:
        abort(404)
    else:
        db.session.delete(pet)
        db.session.commit()
        
        return jsonify({"success": True, "response": "Pet deleted"})
    
            

db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
    