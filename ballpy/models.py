from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# creating your table
class Reptile(db.Model):
    tablename = 'reptiles'
    
    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(250))
    scientific_name = db.Column(db.String(250))
    conservative_status = db.Column(db.String(250))
    native_habitat = db.Column(db.String(250))
    fun_fact = db.Column(db.Text)
 