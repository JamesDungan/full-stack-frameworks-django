from django.urls import path, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('login/', login, name="login"),
    path('register/', registration, name="registration"),
    path('profile/', user_profile, name="user_profile"),
    path('password-reset/', include(url_reset))
]