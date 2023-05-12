from flask import Blueprint, render_template, request, redirect
from . import models 

bp = Blueprint('reptile', __name__, url_prefix='/reptiles')

@bp.route('/')
def index(): 
    return render_template('ballpy/index.html')

@bp.route('/<int:id>')
def show(id): 
    reptile = models.User.query.filter_by(id=id).first()
    
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.common_name,
        'conservative_status': reptile.common_name,
        'native_habitat': reptile.common_name,
        'fun_fact': reptile.common_name,
    }

    return reptile_dict
