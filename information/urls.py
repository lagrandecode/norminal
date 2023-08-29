
from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignupView.as_view(),name='signup'),
    path('staff/',views.StaffInfo.as_view(),name='staff'),
    path('department/',views.DepartmentInfo.as_view(),name='department'),
]
