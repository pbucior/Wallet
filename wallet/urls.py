from django.urls import path
from . import views
from .views import UserOperationsListView, NewOperationView, OperationDeleteView, OperationUpdateView

urlpatterns = [
    path('', UserOperationsListView.as_view(), name='wallet-home'),
    path('operation/new/', NewOperationView.as_view(), name='operation-new'),
    path('operation/<int:pk>/delete', OperationDeleteView.as_view(), name='operation-delete'),
    path('operation/<int:pk>/update', OperationUpdateView.as_view(), name='operation-update'),
]
