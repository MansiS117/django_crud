from django.urls import path
from . import views

urlpatterns = [
    path("" , views.book_list, name = "book_list"),
    path("book/<int:bookid>/" , views.book_detail , name = "book_detail"),
    path("book/new" , views.new_book , name = "new_book"),
    path("book/<int:bookid>/edit" , views.update_book, name = "update_book"),
    path("book/<int:bookid>/delete", views.delete_book , name = "delete_book"),
]