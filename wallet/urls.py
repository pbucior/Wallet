from django.urls import path
from . import views
from .views import UserOperationsListView

urlpatterns = [
    path('', UserOperationsListView.as_view(), name='wallet-home'),
]
