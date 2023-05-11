from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# creating your table
class Fact(db.Model):
    tablename = 'reptiles'
    
    