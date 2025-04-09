from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, CreateView
from .models import Skill, Education, Experience, Contact
from .forms import ContactForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        context['education'] = Education.objects.all()
        context['experience'] = Experience.objects.all()
        return context

class ContactView(TemplateView):
    template_name = 'core/contact.html'
