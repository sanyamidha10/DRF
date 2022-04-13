from rest_framework import serializers
from .models import Student

# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should start with R')
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    
    # Field Level Validation
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower()!='ranchi':
    #         raise serializers.ValidationError('City must be Ranchi')
    #     return data
