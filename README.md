# PY-BALL-API

## Installation venv (virtual enviroment)

- to install venv: `python3 -m venv venv`
- to activate: `. venv/bin/activate`
- to deactivate: `deactivate`

## Installation pip flask

- to install flask: `pip install Flask`
- to run flask: `flask run`
  - "localhost:5000"
  - "http://127.0.0.1:5000/"
- to Constantly reload: `flask run --reload`

## Installint Flask-SQLAlchemy

- to install Flask-SQLAlchemy: `pip install flask-sqlalchemy`
- Migrate tools
  - to migrate: 
    `pip install Flask-Migrate`
  
  - install a Postgres database adapter: 
    `pip install psycopg2-binary`
  
  - Initialize the app for migrations
    `flask db init`
  
  - Generate the migration files
    `flask db migrate`
  
  - Apply the migration to the database
    `flask db upgrade`

## Installing python .evv

- Install .env: `pip install python-dotenv`
- create .env file

<!-- 
from dotenv import load_dotenv
import os # to access environment variables using "os.environ"

load_dotenv() # Load environment variables from .env file 
-->
