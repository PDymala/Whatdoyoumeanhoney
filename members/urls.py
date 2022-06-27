from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('login_out/', views.logout, name='logout'),
    path('signup/', views.signup, name="signup"),
    path('captcha/', include('captcha.urls')),
    path('', include('django.contrib.auth.urls'))
]