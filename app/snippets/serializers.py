from django.forms import widgets
from rest_framework import serializers

from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='Friendly')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        검증한 데이터로 새 "Snippet"인스턴스를 업데이트 한 후 리턴
        :param validated_data:
        :return:
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        isinstance.title = validated_data.get('title', instance.title)
        isinstance.code = validated_data.get('code', instance.code)
        isinstance.linenos = validated_data.get('linenos', instance.linenos)
        isinstance.language = validated_data.get('language', instance.lanuage)
        isinstance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
