from sesion14.app import db

class Author(db.Model):
    id = db.Column("idAuthor", db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    nationality = db.Column(db.String(45))