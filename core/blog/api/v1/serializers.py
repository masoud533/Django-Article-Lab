from rest_framework import serializers
from blog.models import Post, Category

# class postSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','author','title','content','created_date','status','published_date']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']