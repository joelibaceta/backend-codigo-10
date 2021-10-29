from sesion14.app import ma

class BookSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "category_name", "author_list")