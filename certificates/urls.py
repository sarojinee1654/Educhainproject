from django.urls import path
from .views import *

urlpatterns = [    
    path('',home, name='home'),
    path('issue_certificate/',issue_certificate, name='issue_certificate'),
    path('verify_certificate/',verify_certificate, name='verify_certificate'),
]