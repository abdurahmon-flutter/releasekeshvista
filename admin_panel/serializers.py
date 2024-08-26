from rest_framework import serializers
from .models import (
    LearningCenter, 
    AdminUser, 
    LearningCenterDetails, 
    Student, 
    LearningCenterGroupStatus, 
    Teacher, 
    RequestToApply
)


class LearningCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCenter
        fields = [
            'id', 'name', 'appeal_phone_number', 'image', 'location', 'bio', 
            'manager_name', 'manager_phone_number', 'create_date', 'update_date', 
            "manager_password", "login", "password"
        ]


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class LearningCenterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCenterDetails
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class LearningCenterGroupStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCenterGroupStatus
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class RequestToApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestToApply
        fields = '__all__'
