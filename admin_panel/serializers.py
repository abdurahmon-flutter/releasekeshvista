from rest_framework import serializers
from .models import LearningCenter, AdminUser, RequestToApply


class LearningCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningCenter
        fields = ['id', 'name', 'appeal_phone_number', 'image', 'location', 'bio', 'manager_name',
                  'manager_phone_number', 'create_date', 'update_date', "manager_password"]


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'

        
class RequestToApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestToApply
        fields = '__all__'
