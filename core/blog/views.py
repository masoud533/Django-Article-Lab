from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, FormView, CreateView, UpdateView)
from .models import Post
from .forms import CreatePost

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
    paginate_by = 2

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts 

class PostDetail(DetailView):
    model = Post

'''
class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = CreatePost
    success_url = "/blog/post/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
'''

class ContactFormView(CreateView):
    model = Post
    # filds = ['author','title','content', 'status', 'published_date']
    form_class = CreatePost
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = CreatePost
    success_url = '/blog/post/'