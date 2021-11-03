"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import hello_world
from core.views import BooksView
from core.views import BookListView

from core.views import function_book
from core.views import BookDetail
from core.views import BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('books/', BooksView.as_view()),
    path('books2/', BookListView.as_view()),

    path('book/<id>/', function_book),
    path('book2/<id>/', BookDetail.as_view()),
    path('book3/<pk>/', BookDetailView.as_view())
]
