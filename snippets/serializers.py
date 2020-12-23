from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

"""
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
"""

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

    def create(self, validated_data):
        # Create and Return New Snippet, Instance, Given the Validated Data
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        # Update and Return an Existing snippet, Instance, Given the Validated Data
        instance.title = validated_data('title', instance.title)
        instance.code = validated_data('code', instance.code)
        instance.linenos = validated_data('linenos', instance.linenos)
        instance.language = validated_data('langauge', instance.language)
        instance.style = validated_data('style', instance.style)
        instance.save()
        return instance