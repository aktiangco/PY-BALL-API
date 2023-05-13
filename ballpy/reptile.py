from flask import Blueprint, render_template, request, redirect
from . import models 

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

# * INDEX PAGE
@bp.route('/', methods=['GET', 'POST'])
def index(): 
    #* POST method
    if request.method == 'POST':
        # create new reptile 
        new_reptile = models.Reptile(
            common_name = request.form['common_name'],
            scientific_name = request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )
  
        models.db.session.add(new_reptile)
        models.db.session.commit() # commit the new reptile to the database 
        
        return redirect('/reptiles') # redirect to index

    #* GET method 
    found_reptiles = models.Reptile.query.all()  # find all reptiles 

    reptile_dict = {'reptiles': []} # create empty dictionary with an empty list value

    # loop through all reptiles and append it to the list 
    for reptile in found_reptiles:
        reptile_dict["reptiles"].append({
            'common_name': reptile.common_name,
            'scientific_name': reptile.scientific_name,
            'conservation_status': reptile.conservation_status,
            'native_habitat': reptile.native_habitat,
            'fun_fact': reptile.fun_fact
        })

    return reptile_dict # return the dictionary, which will get returned as JSON by default

# * SHOW ID PAGE
@bp.route('/<int:id>')
def show(id): 
    reptile = models.User.query.filter_by(id=id).first() # find the reptile by id
    # create a dictionary of the reptile's information
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.common_name,
        'conservation_status': reptile.common_name,
        'native_habitat': reptile.common_name,
        'fun_fact': reptile.common_name,
    }

    return reptile_dict # return the dictionary, which will get returned as JSON by default

# * Replace or Update ID page
@bp.route('/<int:id>', methods=['PUT'])
def update_reptile(id):
    reptile = models.Reptile.query.get(id)  # find the reptile by id

    if not reptile:
        return {'message': 'Reptile not found.'}, 404

    reptile.common_name = request.form.get('common_name', reptile.common_name)
    reptile.scientific_name = request.form.get('scientific_name', reptile.scientific_name)
    reptile.conservation_status = request.form.get('conservation_status', reptile.conservation_status)
    reptile.native_habitat = request.form.get('native_habitat', reptile.native_habitat)
    reptile.fun_fact = request.form.get('fun_fact', reptile.fun_fact)
    models.db.session.commit()

    return {'message': 'Reptile updated successfully.'}, 200


# * Delete ID page
@bp.route('/<int:id>', methods=['DELETE'])
def delete_reptile(id):
    reptile = models.Reptile.query.get(id)  # find the reptile by id

    if reptile:
        models.db.session.delete(reptile)
        models.db.session.commit()
        return {'message': 'Reptile deleted successfully.'}, 200
    else:
        return {'message': 'Reptile not found.'}, 404
