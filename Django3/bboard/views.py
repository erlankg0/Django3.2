from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Bb, Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm, RubricForm
from django.urls import reverse_lazy
from django.template.loader import get_template, select_template
from django.template.response import TemplateResponse


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
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubric'] = Rubric.objects.all()
        return context


def add(request):
    bbf = BbForm()
    context = {"form": bbf}
    return render(request, 'bboard/create.html', context=context)


def add_save(request):
    bbf = BbForm(request.POST)
    if bbf.is_valid():
        bbf.save()
        from django.urls import reverse
        return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
    else:
        context = {"form": bbf}
        return render(request, 'bboard/create.html', context)


def add_and_save(request):
    if request.method == "POST":
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            from django.urls import reverse
            return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {"form": bbf}

    else:
        bbf = BbForm()
        context = {"form": bbf}
        return render(request, 'bboard/create.html', context)


def low_index(request):
    resp = HttpResponse(content="здесь будет!", content_type='text/plain; charset=urf-8')
    resp.write(' Main')
    resp.writelines((' page', ' site'))
    resp['keywords'] = 'Python, Django'
    return resp


def high_index(request):
    bbs = Bb.objects.all()
    rubric = Rubric.objects.all()
    context = {'bbs': bbs, 'rubric': rubric}
    template = get_template('bboard/def_index.html')
    return HttpResponse(template.render(context=context, request=request))


def templateResponse_index(request, pk='Авто'):
    bbs = Bb.objects.all()
    rubric = Rubric.objects.all()
    context = {'bbs': bbs, 'rubric': rubric, 'http': print(request.POST)}
    template = get_template('bboard/def_index.html')
    return TemplateResponse(request, template, context)
