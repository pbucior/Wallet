from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Operation

def home(request):
    context = {
        'operations': Operation.objects.all()
    }
    return render(request, 'home.html', context)

class UserOperationsListView(LoginRequiredMixin, ListView):
    model = Operation
    template_name = 'home.html'
    context_object_name = 'operations'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Operation.objects.filter(user=user).order_by('-date_operation', '-date_added')
