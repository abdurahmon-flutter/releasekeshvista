from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from admin_panel.models import LearningCenter
from admin_panel.serializers import LearningCenterSerializer


@api_view(["GET", "POST", "HEAD", "OPTIONS"])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/clients/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of clients'
        },
        {
            'Endpoint': '/clients/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single client'
        },
        {
            'Endpoint': '/clients/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new client'
        },
        {
            'Endpoint': '/clients/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates a client'
        },
        {
            'Endpoint': '/clients/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a client'
        },
    ]
    return Response(routes)


class LearningCenterListCreateView(generics.ListCreateAPIView):
    queryset = LearningCenter.objects.all()
    serializer_class = LearningCenterSerializer


class LearningCenterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearningCenter.objects.all()
    serializer_class = LearningCenterSerializer
