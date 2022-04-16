from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Todo
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class Homepage(TemplateView):

    template_name = "htmls/Homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = 'Activitylist'
        return context

class DateCreateView(CreateView):

    model = Todo,
    fields = '__all__',
    template_name = "htmls/DateCreateView.html",
    success_url = reverse_lazy('')

