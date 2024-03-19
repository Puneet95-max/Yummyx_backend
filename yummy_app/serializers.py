from  rest_framework import serializers
from .models import chef_table, testimonial_table
from django.contrib.auth.models import User

class chef_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = chef_table
        fields = "__all__"
        
class testimonial_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = testimonial_table
        fields = "__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
