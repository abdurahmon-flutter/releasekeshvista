from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from admin_panel.models import LearningCenter, AdminUser, LearningCenterGroupStatus, RequestToApply,LearningCenterDetails,Student,Teacher,checkBalance
from admin_panel.serializers import *
from rest_framework.permissions import AllowAny
from django.utils import timezone
from rest_framework import status
@api_view(["GET", "POST", "HEAD", "OPTIONS"])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/clients/',
        },
    ]
    return Response(routes)


class LearningCenterListCreateView(generics.ListCreateAPIView):
    queryset = LearningCenter.objects.all()
    serializer_class = LearningCenterSerializer


class LearningCenterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningCenter.objects.all()
    serializer_class = LearningCenterSerializer


class AdminUserListCreate(generics.ListCreateAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer


class AdminUserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer


class RequestListCreate(generics.ListCreateAPIView):
    queryset = RequestToApply.objects.all()
    serializer_class = RequestToApplySerializer

class CurrentbalanceView(APIView):
    permission_classes = [AllowAny]
    
    def tolovlar(self, balance, tolovlar_queryset):
        current_month = timezone.now().month
        current_year = timezone.now().year
        
        for tolov in tolovlar_queryset:
            if (tolov.status == "UNPAID" and 
                current_month - tolov.paymentMonthlyPeriod <= tolov.lastPayedMonth):
                balance -= tolov.paymentAmount
                
                tolov.status = "PAID"
                tolov.save()               
                
        return balance

    def get(self, request):
        balance = 120.5
        debt = 0
     
        # Adjust balance based on payment status
        balance = self.tolovlar(balance, LearningCenterGroupStatus.objects.all())
        
        current_time = timezone.now()
        
        return Response({
            'balance': balance,
            'debt': debt,
            'current_time': current_time
        })
        
            
       
class RequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestToApply.objects.all()
    serializer_class = RequestToApplySerializer


class LCenterGroupDetailListCreate(generics.ListCreateAPIView):
    serializer_class = LearningCenterGroupStatusSerializer

    def get_queryset(self):
        queryset = LearningCenterGroupStatus.objects.all()
        
        for instance in queryset:
            current_year = timezone.now().year
            current_month = timezone.now().month
            
            # Update status if payment is due
            if (instance.nextPaymentYear < current_year) or (instance.nextPaymentYear == current_year and instance.nextPaymentMonth <= current_month):
                instance.status = "UNPAID"
                instance.save()
                
                # Check if balance can cover the payment
                unpaid_queryset = LearningCenterGroupStatus.objects.filter(
                    learningCenterDetailID=instance.learningCenterDetailID,
                    status="UNPAID"
                )
                
                total_payment_due = sum(unpaid.paymentAmount for unpaid in unpaid_queryset)
                
                if checkBalance(learningCenterDetailID=instance.learningCenterDetailID, payment=total_payment_due):
                    lcenter_detail = LearningCenterDetails.objects.get(id=instance.learningCenterDetailID)
                    lcenter_detail.balance -= total_payment_due
                    lcenter_detail.save()
                    
                    # Update the payment status and next payment date
                    for unpaid in unpaid_queryset:
                        unpaid.status = "PAID"
                        unpaid.lastPayedYear = current_year
                        unpaid.lastPayedMonth = current_month
                        
                        next_month = current_month + unpaid.paymentPeriod
                        unpaid.nextPaymentMonth = next_month if next_month <= 12 else next_month - 12
                        unpaid.nextPaymentYear = current_year if next_month <= 12 else current_year + 1
                        unpaid.save()

        return queryset
    
    def perform_create(self, serializer):
        instance = serializer.save()
        self.check_and_update_payment_amount(instance)

    def check_and_update_payment_amount(self, instance):
        if instance.id == 2:
            instance.paymentAmount = 100
            instance.save()


class LCenterGroupDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningCenterGroupStatus.objects.all()
    serializer_class = LearningCenterGroupStatusSerializer
    def perform_update(self, serializer):
        instance = serializer.save()
        self.check_and_update_payment_amount(instance)
    def check_and_update_payment_amount(self, instance):
        if instance.id == 2:
            instance.paymentAmount = 100
            instance.save()    
class LCenterDetailListCreate(generics.ListCreateAPIView):
    queryset = LearningCenterDetails.objects.all()
    serializer_class = LearningCenterDetailsSerializer


class LCenterDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningCenterDetails.objects.all()
    serializer_class = LearningCenterDetailsSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer       
class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer          