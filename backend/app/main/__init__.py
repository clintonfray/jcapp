from flask import Blueprint

bp = Blueprint('ain', __name__)

from app.main import routes
