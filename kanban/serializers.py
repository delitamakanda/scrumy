import datetime

from rest_framework import serializers
from .models import List, Card, Todo
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):
    tag_name = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = '__all__'

    def get_tag_name(self, obj):
        return obj.get_tag_display()


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = '__all__'



class UsersSerializer(serializers.ModelSerializer):
    lists = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())

    class Meta:
        model = User
        fields = '__all__'
