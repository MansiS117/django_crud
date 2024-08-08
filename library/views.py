from django.shortcuts import render , redirect , get_object_or_404
from .forms import BookForm
from .models import Book

# Create your views here.
def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
        form = BookForm()
    return render(request , "book_form.html" , {"form" : form})


def book_list(request):
    books = Book.objects.all()
    return render(request ,"book_list.html" , {"books": books})

def book_detail(request , bookid):
    book = get_object_or_404(Book , id=bookid)
    return render(request , "book_detail.html" , {"book" : book})


def update_book(request , bookid):
    book = get_object_or_404(Book , id=bookid)
    if request.method == "POST":
        form = BookForm(request.POST , instance = book)
        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
        form = BookForm(instance = book)
    return render(request , "book_form.html" , {"form" : form})

def delete_book(request , bookid):
    book = get_object_or_404(Book , id = bookid)
    if request.method == "POST":
        book.delete()
        redirect("book_list")

    return render(request , "book_delete.html" , {"book" : book})
