from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from admin_panel.models import LearningCenter, AdminUser, RequestToApply
from admin_panel.serializers import LearningCenterSerializer, AdminUserSerializer, RequestToApplySerializer


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


class RequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestToApply.objects.all()
    serializer_class = RequestToApplySerializer
