from rest_framework import serializers
from .models import Keyword, Flag


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class FlagSerializer(serializers.ModelSerializer):
    keyword_name = serializers.CharField(source='keyword.name', read_only=True)
    content_title = serializers.CharField(source='content_item.title', read_only=True)

    class Meta:
        model = Flag
        fields = '__all__'