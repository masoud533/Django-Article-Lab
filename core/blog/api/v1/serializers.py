from rest_framework import serializers
from blog.models import Post, Category

"""--- Serializers define the API representation. ---"""

# class postSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class PostSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id','author','title','content', 'category','absolute_url','created_date','status','published_date']
        # read_only_fields = ['content']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']