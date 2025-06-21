from .models import Snippet, Tag
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class SnippetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    highlighted = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Snippet
        fields = [
            'id', 'title', 'language', 'code', 'description',
            'created_at', 'updated_at', 'share_uuid', 'user',
            'highlighted', 'tags'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'share_uuid', 'user']

    def get_highlighted(self, obj):

        try:
            lexer = get_lexer_by_name(obj.language)
            formatter = HtmlFormatter(style="friendly", full=True)
            return highlight(obj.code, lexer, formatter)
        except:
            return obj.code

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        snippet = Snippet.objects.create(**validated_data)
        self._handle_tags(snippet, tags_data)
        return snippet

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        self._handle_tags(instance, tags_data)
        return instance

    def _handle_tags(self, snippet, tags_data):
        user = self.context['request'].user
        snippet.tags.clear()
        for tag_data in tags_data:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_data['name'], user=user)
            snippet.tags.add(tag_obj)