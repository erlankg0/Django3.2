from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm


def index(request):
    obj = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {"bboard": obj, "rubrics": rubrics}
    return render(request, "bboard/index.html", context=context)


def by_rubric(request, rubric_id):
    obj = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {"bboard_obj": obj, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(request, "bboard/by_rubric.html", context=context)


# Create your views here.

class BbCreatView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = "/bboard/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubric'] = Rubric.objects.all()
        return context
