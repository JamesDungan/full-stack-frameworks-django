from django.conf.urls import url
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', PasswordResetView, {'post_reset_redirect': reverse_lazy('PasswordResetDoneView')}, name='password_reset'),
    path('done/', PasswordResetDoneView, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView,
        {'post_reset_redirect': reverse_lazy('PasswordResetCompleteView')}, name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView, name='password_reset_complete')
]