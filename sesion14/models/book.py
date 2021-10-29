from sesion14.app import db

class Book(db.Model):

    id          = db.Column("idBook", db.Integer, primary_key = True)
    title       = db.Column(db.String(100))
    nro_pages   = db.Column(db.Integer)
    plot        = db.Column(db.String(250))
    editorial   = db.Column(db.String(45))
    isbn        = db.Column(db.String(45))
    pub_date    = db.Column(db.Date)
    edition     = db.Column("edicion", db.String(45))