from sesion13.app import ma

class MovieSchema(ma.Schema):
    class Meta:
        fields=("title", "year", "length", "director", "updated_at", "created_at")