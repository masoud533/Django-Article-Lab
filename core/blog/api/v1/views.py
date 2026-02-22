from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import postSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404


@api_view()
def postlist(request):
    return Response('ok')

@api_view()
def postDetail(request, id):

    post = get_object_or_404(Post,pk=id)

    serializer = postSerializer(post)
    return Response(serializer.data)