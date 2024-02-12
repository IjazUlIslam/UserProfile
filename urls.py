from django.urls import path
from UserProfile import views

urlpatterns = [
    path('signup/', views.sign_up),
    path('login/', views.user_login),
    path('profile/', views.user_profile),
    path('logout/', views.user_logout),
    path('change-password/', views.user_change_pass, name='changepass'),

]
