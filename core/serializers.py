from rest_framework import serializers
from core.models import Post


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            value, _ = self.get_queryset().get_or_create(**{self.slug_field: data})
            return value    
        except (TypeError, ValueError):
            self.fail("invalid")


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title', 'author', 'text_body', 'created_at', 'updated_at',)