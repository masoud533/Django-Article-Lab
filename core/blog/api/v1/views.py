from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import postSerializer
from blog.models import Post

@api_view()
def postlist(request):
    return Response('ok')

@api_view()
def postDetail(request, id):

    post = Post.objects.get(pk=id)

    serializer = postSerializer(post)
    return Response(serializer.data)