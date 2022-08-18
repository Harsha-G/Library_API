from importlib.resources import path
from django.conf.urls import url, include
from django.urls import path
from endpoint.views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path(r"add_book/", Add_Book.as_view()),
    path(r"delete_all_book/", Delete_All_Books.as_view()),
    path(r"list_books/", List_Books.as_view({'get':'list'})),
    path(r"get_book_count/", Get_BookCount.as_view()),
    path(r"get_book_titles/", Get_Book_Titles.as_view()),
    path(r"get_book_by_author/", Get_Book_By_Author.as_view()),
    path(r"get_book_by_genre/", Get_Book_By_Genre.as_view()),
]