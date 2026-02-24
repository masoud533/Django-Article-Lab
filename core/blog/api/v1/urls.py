from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register('post3', views.PostViewSet,basename='post3')


urlpatterns = [

    # path('post/', views.postlist, name='post-list'),
    # path('post/<int:id>/', views.postDetail, name='post-detail'),

    path('post/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'), 

    path('post2/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list2'),
    path('post2/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update','delete':'destroy'}), name='post-detail2'),
]

urlpatterns += router.urls