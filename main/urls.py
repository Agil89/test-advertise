from django.urls import path
from .views import UpdateStatus

urlpatterns = [
    path('update', UpdateStatus.as_view(), name='update'),
]