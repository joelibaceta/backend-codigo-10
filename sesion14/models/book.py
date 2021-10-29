from sqlalchemy.orm import relationship
from sesion14.app import db

from sesion14.models.authorbook import authors_indentifier

class Book(db.Model):

    id          = db.Column("idBook", db.Integer, primary_key = True)
    title       = db.Column(db.String(100))
    nro_pages   = db.Column(db.Integer)
    plot        = db.Column(db.String(250))
    editorial   = db.Column(db.String(45))
    isbn        = db.Column(db.String(45))
    pub_date    = db.Column(db.Date)
    edition     = db.Column("edicion", db.String(45))
    id_category = db.Column("idCategory", db.Integer, db.ForeignKey('category.idCategory'))
    category    = relationship("Category", back_populates="books")
    authors     = relationship("Author", secondary=authors_indentifier)

    @property
    def category_name(self):
        return self.category.name

    @property
    def author_list(self):
        author_names = map(lambda x: f"{x.first_name} {x.last_name}", self.authors )
        return ", ".join(author_names)