from rest_framework import serializers
from blog.models import Post

# class postSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class postSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id','title','content','created_date','status','published_date']