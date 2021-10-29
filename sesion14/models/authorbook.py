from sesion14.app import db

authors_indentifier = db.Table('AuthorBook',
    db.Column('idAuthor', db.ForeignKey('author.idAuthor')),
    db.Column('idBook', db.ForeignKey('book.idBook')),
)