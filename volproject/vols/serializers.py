from rest_framework import serializers
from .models import Latest_categories, Sentence

class latest_categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latest_categories
        fields = (
            'name',
            'slug',
            'vol_list',
            'date_added',
            'get_absolute_url',
        )

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = (
            'name',
            'word',
            'source',
        )
