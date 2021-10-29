from sesion14.app import ma

class CategorySchema(ma.Schema):
    class Meta:
        fields = ("id", "name")