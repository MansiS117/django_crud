from django.shortcuts import render , redirect , get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.
# create
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    if request.method == "GET":
        form = PostForm()
    return render(request , 'post_form.html' , {"form": form})

# read

def post_list(request):
    posts = Post.objects.all()
    return render(request , 'post_list.html' , {"posts" : posts})

def post_detail(request , pk):
    post = get_object_or_404(Post , pk = pk)
    return render(request , 'post_detail.html' , {"post" : post})


#update

def update_post(request , pk):
    post = get_object_or_404(Post , pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST , instance = post)
        if form.is_valid(): 
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance = post)
    return render(request , "post_form.html" , {"form" : form})

#delete

def delete_post(request , pk):
    post = get_object_or_404(Post , pk = pk)
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request , "post_confirm_delete.html" , {"post" : post})

    

