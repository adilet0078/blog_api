from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from like.serialziers import FavoriteSerializer
from . import serialziers


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serialziers.RegisterSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list':
            return serialziers.UserListSerializer
        return serialziers.UserDetailSerializer

    @action(['GET'], detail=False)
    def favorites(self, request):
        user = request.user
        fav_posts = user.favorites.all()
        serializer = FavoriteSerializer(fav_posts, many=True)
        return Response(serializer.data, status=200)


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serialziers.UserListSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#
# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serialziers.UserDetailSerializer
#     permission_classes = (permissions.IsAuthenticated,)

