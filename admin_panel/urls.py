from django.urls import path
from . import views
from .views import LearningCenterListCreateView, LearningCenterDetailView

urlpatterns = [
    path('',views.getRoutes),
    path('clients/', LearningCenterListCreateView.as_view(), name='learning-center-list-create'),
    path('clients/<int:pk>/', LearningCenterDetailView.as_view(), name='learning-center-detail'),

]
