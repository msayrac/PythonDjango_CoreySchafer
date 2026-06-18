from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post
from blog.api.serializers import PostSerializer
from rest_framework import status # durum kodları için gereklidir


class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)
    
    # dışarıdan gelen veri
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        # veri kurallara uygun mu data=request.data uygun mu
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


