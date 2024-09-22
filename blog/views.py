from django.shortcuts import render
from blog.models import Post, Category
from django.shortcuts import redirect
from django.views.generic import CreateView

# Create your views here.


def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats,
    }
    return render(request,'home.html',data)


def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request,'posts.html',{'post':post, 'cats':cats})


def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})


def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts=Post.objects.filter(title__contains=searched)
        return render(request, 'search_posts.html', 
                      { 'searched':searched,
                        'posts':posts})
    else:
      return render(request, 'search_posts.html',{})
    

class AddPostView(CreateView):

    model = Post
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
    