from rest_framework import serializers
from like.models import Like, Favorite


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        post = attrs['post']
        if user.likes.filter(post=post).exists():
            raise serializers.ValidationError(
                'You already liked this post!')
        return attrs


class LikeUserSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        exclude = ('post',)


class FavoriteSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Favorite
        fields = ('id', 'post', 'post_title')

    def to_representation(self, instance):
        repr = super(FavoriteSerializer, self).to_representation(instance)
        preview = instance.post.preview
        repr['post_preview'] = preview.url if preview else None
        return repr

