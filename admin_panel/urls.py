from django.urls import path
from . import views
from .views import CurrentbalanceView, LearningCenterListCreateView, LearningCenterDetailView, AdminUserListCreate, \
    AdminUserRetrieveUpdateDestroy

urlpatterns = [
    path('', views.getRoutes),
    path("lcenterdetail/", views.LCenterDetailListCreate.as_view()),
    path('lcenterdetail/<int:pk>/', views.LCenterDetailRetrieveUpdateDestroy.as_view()),
    path("lcentergroupstatus/", views.LCenterGroupDetailListCreate.as_view(), name="group_status"),
    path("lcentergroupstatus/<int:pk>/", views.LCenterGroupDetailRetrieveUpdateDestroy.as_view(), name="group_status-detail"),
    path('clients/', LearningCenterListCreateView.as_view(), name='learning-center-list-create'),
    path('clients/<int:pk>/', LearningCenterDetailView.as_view(), name='learning-center-detail'),
    path('adminusers/', AdminUserListCreate.as_view(), name='adminuser-list-create'),
    path('adminusers/<int:pk>/', AdminUserRetrieveUpdateDestroy.as_view(), name='adminuser-detail'),
    path("request/", views.RequestListCreate.as_view(), name="request-list-create"),
    path("request/<int:pk>/", views.RequestRetrieveUpdateDestroy.as_view(), name="request-detail-update"),
    path("students/",views.StudentListCreate.as_view(),name="lmqwl,x;qmx"),
    path("students/<int:pk>",views.StudentRetrieveUpdateDestroy.as_view(),name="lmqwl,x;qmx-dteail"),
    path("teachers/<int:pk>/",views.TeacherRetrieveUpdateDestroy.as_view(),name="teachers-dteail"),
    path("teachers/",views.TeacherListCreate.as_view(),name="teachers"),
    path("current-time/",views.CurrentbalanceView.as_view(),name="mkxkqw"),
    path("parents/",views.ParentListCreate.as_view(),name="parent_list_create"),
    path("parents/<int:pk>",views.ParentRetrieveUpdateDestroy.as_view(),name="parent_update_delete")
]
