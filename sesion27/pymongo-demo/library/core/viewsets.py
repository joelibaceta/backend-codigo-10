from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from core.models import Book

class BooksView(ViewSet): 

    def create(self, request):
        data = request.data
        print(data)
        book = Book()
        book.insert(data)
        return Response(status=status.HTTP_201_CREATED)


    def list(self, request):
        title = request.GET.get("title")
        if title == None:
            books = Book.all()
        else:
            books = Book.find_by_title(title)
        return Response(books)

    def search(self, request):
        query = request.GET.dict()
        print(query)
        books = Book.search(query)
        return Response(books)
