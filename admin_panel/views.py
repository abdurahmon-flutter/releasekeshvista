from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from admin_panel.models import LearningCenter, AdminUser
from admin_panel.serializers import LearningCenterSerializer, AdminUserSerializer


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
