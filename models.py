"""Models for Blogly."""

from flask.helpers import get_template_attribute
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEF_IMG_URL = "https://www.freeiconspng.com/uploads/user-group-flat-icon-png-24.png" 

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=True, default=DEF_IMG_URL)

    @property
    def full_name(self):
        """retrieve user full name"""
        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """connect to flask"""
    db.app = app
    db.init_app(app)