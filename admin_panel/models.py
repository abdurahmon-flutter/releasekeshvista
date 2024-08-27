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
    manager_password = models.CharField(max_length=255)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Normally you'd use Django's User model for better security

    def __str__(self):
        return self.name





class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentPhone_number = models.CharField(max_length=20)
    studentImage = models.ImageField(upload_to='students/', blank=True, null=True)
    studentBio = models.TextField(),
    parentId = models.IntegerField()
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.studentName


class LearningCenterGroupStatus(models.Model):
    learningCenterDetailID = models.IntegerField()
    learningCenterGroupId = models.IntegerField()
    learningCenterID = models.IntegerField()
    studentID = models.IntegerField()
    paymentAmount = models.FloatField()
    status = models.CharField(max_length=250)
    nextPaymentMonth = models.IntegerField()
    nextPaymentYear = models.IntegerField()
    paymentPeriod = models.IntegerField()
    lastPayedMonth = models.IntegerField()
    lastPayedYear = models.IntegerField()
    def __str__(self):
        return str(self.learningCenterGroupId)

def checkBalance(learningCenterDetailID,payment):
    balance = 0
    lcenter_detail_queryset = LearningCenterDetails.objects.all()
    
    for lcenter_detail in lcenter_detail_queryset:
        if(lcenter_detail.id==learningCenterDetailID):
            balance = lcenter_detail.balance
    if(balance<=payment):
        return False
    else:
        return True
class LearningCenterDetails(models.Model):
    learningCenterId = models.IntegerField()
    balance = models.FloatField()
    debt = models.FloatField()
    studentId = models.IntegerField()

    def __str__(self):
        return str(self.studentId)
class Teacher(models.Model):
    teacherName = models.CharField(max_length=100)
    teacherPhone_number = models.CharField(max_length=20)
    teacherImage = models.ImageField(upload_to='teachers/', blank=True, null=True)
    teacherBio = models.TextField()
    teacherAge = models.IntegerField()
    learningCenterIDsList = models.JSONField(default=list)

    def __str__(self):
        return self.teacherName


class RequestToApply(models.Model):
    name = models.CharField(max_length=100)
    leaningCenterName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
class Parent(models.Model):
    fatherName = models.CharField(max_length=250)
    motherName = models.CharField(max_length=250)
    fatherPhone = models.CharField(max_length=250)
    motherPhone = models.CharField(max_length=250)
    fatherImage = models.CharField(max_length=250)
    motherImage = models.CharField(max_length=250)
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__ (self):
        return self.fatherName