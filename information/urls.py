
from django.urls import path
from . import views

urlpatterns = [
    path('',views.SignupView.as_view(),name='signup'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('info/',views.UserInfo.as_view(),name='info'),
    path('staff/',views.StaffUser.as_view(),name='staff'),

]
