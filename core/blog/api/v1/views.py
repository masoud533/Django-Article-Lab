from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

""" funtion base view """
# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# def postlist(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = postSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = postSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# @api_view(["GET", "PUT", "DELETE"])
# def postDetail(request, id):
#     post = get_object_or_404(Post,pk=id,status=True)

#     if request.method == "GET":
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == "DELETE":
#         post.delete()
#         return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

"""--- class base view  ---"""

""" API View """

# class PostList(APIView):
#     """ getting a list of posts and creating new posts"""

#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self,request):
#         """ retriveing a list of posts"""
#         posts = Post.objects.filter(status=True)
#         serializer = self.serializer_class(posts,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         '''creatins a post with provided data'''
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

    
# class PostDetail(APIView):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self,request,id):
#         """ retriveing the post data """
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         """ editing the post data """
#         post = get_object_or_404(Post,pk=id,status=True)
#         serializer = self.serializer_class(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,id):
#         """ deleting the post object"""
#         post = get_object_or_404(Post,pk=id,status=True)
#         post.delete()
#         return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT) 


""" Generics View """

class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


# class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     """ getting detail of the post and edit plus removing it """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         """ editing the post data """
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         """ deleting the post object"""
#         return self.destroy(request, *args, **kwargs)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


"""--- ViewSet ---"""

class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass 
