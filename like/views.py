from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Like
from .serialziers import LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDeleteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request):
        if 'post' not in request.data:
            return Response({'message': 'Field "post" is required!'},
                            status=400)

        post = request.data.get('post')
        user = request.user
        like = user.likes.filter(post=post)
        if not like.exists():
            return Response({'message': 'You didn\'t like this post!'},
                            status=400)
        like.delete()
        return Response({'message': 'deleted!'}, status=204)


