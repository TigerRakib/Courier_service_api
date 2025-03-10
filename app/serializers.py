from rest_framework import serializers
from app.models import Package

class Package_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
