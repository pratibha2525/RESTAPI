from dataclasses import field, fields
from rest_framework import serializers
from myapp.models import empmodel,cricketmodel

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = empmodel
        fields = ('emp_id','emp_name','emp_course')

class cricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = cricketmodel
        fields = ('id','name')