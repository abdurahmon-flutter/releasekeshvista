from django.db import models


class LearningCenter(models.Model):
    name = models.CharField(max_length=255)
    appeal_phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='learning_centers/', blank=True, null=True)
    location = models.CharField(max_length=255)
    bio = models.TextField()
    manager_name = models.CharField(max_length=255)
    manager_phone_number = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Normally you'd use Django's User model for better security

    def __str__(self):
        return self.name
