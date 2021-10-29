from sqlalchemy.orm import relationship
from sesion14.app import db

class Category(db.Model):

    id = db.Column("idCategory", db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    books = relationship("Book", back_populates="category")