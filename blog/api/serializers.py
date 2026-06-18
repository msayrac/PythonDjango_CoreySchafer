from rest_framework import serializers
from blog.models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)
    date_posted = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        
        fields = ['id','title','content','date_posted','author']





