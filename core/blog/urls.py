from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = "blog"

urlpatterns = [
    path('fbv-index', views.indexView, name="fbv-test"),
    path('cbv-index', views.IndexView.as_view(), name="cbv-test"),
    path('post/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/create/', views.ContactFormView.as_view(), name='post-create'),
    path('go-to-index', RedirectView.as_view(pattern_name="blog:cbv-test"), name="redirect-to-index")
]