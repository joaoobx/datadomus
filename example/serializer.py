from rest_framework import serializers
from .models import Example
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id','title']