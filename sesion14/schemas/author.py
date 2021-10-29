from sesion14.app import ma

class AuthorSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "nationality")