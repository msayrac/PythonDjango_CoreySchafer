from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post
from blog.api.serializers import PostSerializer
from rest_framework import status # durum kodları için gereklidir
from rest_framework.generics import get_object_or_404

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
    
class PostDetailAPIView(APIView):
    def get_object(self,pk):
        post_instance = get_object_or_404(Post, pk=pk)
        return post_instance
    
    def get(self, request,pk):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(instance = post)
        return Response(serializer.data)
    
    def put(self,request, pk):
        post = self.get_object(pk=pk)
        serializer = PostSerializer(instance = post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
