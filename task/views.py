from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class CustomerLogin(LoginView):
    template_name = 'task/login.html'
    fields = '__all__' 
    redirect_authenticated_user = True
     
     
    def get_success_url(self):
        return reverse_lazy('tasks')   
    
class RegisterPage(FormView):
    form_class = UserCreationForm
    template_name = 'task/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)   
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args,**kwargs)
        
         
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(customer=self.request.user)
        
        search_input = self.request.GET.get('search') or ""
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith = search_input)
        context['search_input'] = search_input    
        return context
        
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
      
class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(CreateTaskView, self).form_valid(form)
    
class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task  
    success_url = reverse_lazy('tasks')
    
      