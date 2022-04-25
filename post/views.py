from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from post.models import Post
from post.serializers import PostCreationSerializer, PostListSerializer


# Create/Update/Delete View
class PostCRUD(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        try:
            owner = data.get("owner")
            content = data.get("content")
            title = data.get("title")
            likes = data.get("likes")

            post = Post.objects.create(owner=User.objects.get(pk=request.user.id), title=title, content=content)
            if post is not None:
                return Response({"detail": f"{title} Post Successfully Created",
                                 "data": PostCreationSerializer(post).data})

            return Response({"detail": "Something Occurred"}, status=status.HTTP_400_BAD_REQUEST)

        except (Exception, ) as err:
            return Response({"Error": f"An error occurred - {str(err)}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        try:
            if not slug:
                return Response({"detail": "Pass a post's slug to Delete"}, status=status.HTTP_400_BAD_REQUEST)

            post = Post.objects.get(slug=slug)
            if post is None:
                return Response({"detail": "Could not get this Post"}, status=status.HTTP_400_BAD_REQUEST)

            post.delete()
            return Response({"detail": "Post has been deleted"})

        except (Exception, ) as err:
            return Response({"detail": "An error occurred"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug):
        try:
            title = request.data.get('title')
            content = request.data.get('content')

            if not slug:
                return Response({"detail": "Pass a post's slug to Update"}, status=status.HTTP_400_BAD_REQUEST)

            if not (title and content):
                return Response({"detail": "Requires a title or content to update"}, status=status.HTTP_400_BAD_REQUEST)

            post = get_object_or_404(Post, slug=slug)
            if post is None:
                return Response({"detail": "Could not get this Post"}, status=status.HTTP_400_BAD_REQUEST)

            post.title = title
            post.content = content
            post.save()

            return Response({"detail": "Post has been Updated", "data":PostCreationSerializer(post).data})

        except (Exception, ) as err:
            return Response({"detail": "An error occurred"}, status=status.HTTP_400_BAD_REQUEST)


# Like Post
class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        try:
            if not slug:
                return Response({"detail": "Pass a post's slug to like"})

            post = Post.objects.get(slug=slug)

            if post is not None:
                post.likes.add(request.user)
                post.save()
                return Response({"detail": f"Post has been Liked by {request.user} -- ",
                                 "data": f"Total Likes: {post.likes.count()}"})

        except (Exception, ) as err:
            return Response({"detail": "An error occurred"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Something Unexpected Happened"}, status=status.HTTP_400_BAD_REQUEST)


#  List All Post
class PostList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            query_set = Post.objects.all().order_by('published')
            # p = Post.objects.get(pk=22)
            # print(p, p.add_likes_count(), p.likes_count)
            serializer = PostListSerializer(query_set, many=True).data
            return Response({"Total Post": f"{query_set.count()}",
                             "detail": serializer})
        except (Exception, ) as err:
            return Response({"detail": "An error occurred", "data": str(err)})
