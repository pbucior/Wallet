from django.urls import path
from . import views
from .views import UserOperationsListView, NewOperationView

urlpatterns = [
    path('', UserOperationsListView.as_view(), name='wallet-home'),
    path('operation/new/', NewOperationView.as_view(), name='operation-new'),
]
