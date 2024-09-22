from blog.models import Post
from django.views.generic import CreateView, UpdateView



class add_posts(CreateView):
    model = Post
    template_name = 'add_posts.html'
    fields = ('post_id','title','image','url','cat','content','snippet')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_posts.html'
    fields = ('post_id','title','image','url','cat','content','snippet')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    





  