from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
from .models import Operation
from .forms import UserRegisterForm

def home(request):
    context = {
        'operations': Operation.objects.all()
    }
    return render(request, 'home.html', context)

class UserOperationsListView(LoginRequiredMixin, ListView):
    model = Operation
    template_name = 'home.html'
    context_object_name = 'operations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.request.user)
        operations = Operation.objects.filter(user=user)
        debit = 0
        credit = 0
        for operation in operations:
            if operation.posting_key == 0:
                debit += operation.amount
            else:
                credit += operation.amount
        balance = credit - debit
        context['balance'] = balance
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Operation.objects.filter(user=user).order_by('-date_operation', '-date_added')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto dla użytkownika {username} zostało utworzone!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class NewOperationView(LoginRequiredMixin, CreateView):
    model = Operation
    fields = ['date_operation', 'amount', 'description', 'posting_key']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OperationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Operation
    success_url = '/'

    def test_func(self):
        operation = self.get_object()
        if self.request.user == operation.user:
            return True
        return False

class OperationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Operation
    fields = ['date_operation', 'amount', 'description', 'posting_key']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        operation = self.get_object()
        if self.request.user == operation.user:
            return True
        return False
