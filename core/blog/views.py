from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post

def indexView(request):
    return render(request,"index.html")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'masoud'
        context['posts'] = Post.objects.all()
        return context
    
class PostList(ListView):
    # model = Post
    # queryset = Post.object.all()
    context_object_name = 'posts'

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts 