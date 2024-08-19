from django.urls import path
from . import views
from .views import LearningCenterListCreateView, LearningCenterDetailView, AdminUserListCreate, \
    AdminUserRetrieveUpdateDestroy

urlpatterns = [
    path('', views.getRoutes),
    path('clients/', LearningCenterListCreateView.as_view(), name='learning-center-list-create'),
    path('clients/<int:pk>/', LearningCenterDetailView.as_view(), name='learning-center-detail'),
    path('adminusers/', AdminUserListCreate.as_view(), name='adminuser-list-create'),
    path('adminusers/<int:pk>/', AdminUserRetrieveUpdateDestroy.as_view(), name='adminuser-detail'),
    path("request/", views.RequestListCreate.as_view(), name="request-list-create"),
    path("request/<int:pk>/", views.RequestRetrieveUpdateDestroy.as_view(), name="request-detail-update"),
]
