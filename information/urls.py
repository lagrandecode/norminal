
from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignupView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('staff/',views.StaffInfo.as_view(),name='staff'),
]
