from sesion11.app import db

class Movie(db.Model):
    id = db.Column("idMovie", db.Integer, primary_key = True)
    title = db.Column("Title", db.String(45))
    plot = db.Column("Plot", db.String(250))
    year = db.Column("Year", db.Integer)
    length = db.Column("Length", db.Integer)
    director = db.Column("Director", db.String(45))
    background_image = db.Column("BackgroundImage", db.String(250))
    cover_image = db.Column("CoverImage", db.String(250))
    main_color = db.Column("MainColor", db.String(45))


    def create_movie(**kwargs):
        new_movie = Movie(**kwargs)
        db.session.add(new_movie)
        db.session.commit()

