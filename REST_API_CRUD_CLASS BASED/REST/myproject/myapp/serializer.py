from dataclasses import field
from rest_framework import serializers
from myapp.models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','address','student')