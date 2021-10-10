from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb, Rubric, Salesman
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
    'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

def by_salesman(request, salesman_id):
    bbs = Bb.objects.filter(person=salesman_id)
    rubrics = Rubric.objects.all()
    current_salesman = Salesman.objects.get(pk=salesman_id)
    context = {'bbs' : bbs, 'rubrics' : rubrics, 'current_salesman' : current_salesman}
    return render(request, 'bboard/by_salesman.html', context)

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    salesmen = Salesman.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics, 'salesmen' : salesmen}
    return render(request, 'bboard/index.html', context)

def title_page(request):
    bbs = Bb.objects.all()[:2]
    context = {'bbs': bbs}
    return render(request, "bboard/title_page.html", context)