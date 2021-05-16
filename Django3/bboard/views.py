from django.http import FileResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, SingleObjectMixin
from .forms import BbForm
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator

def index(request):
    obj = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {"bboard": obj, "rubrics": rubrics}
    return render(request, "bboard/index.html", context=context)


class BbCreatView(CreateView):
    template_name = 'bboard/index.html'
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
            return HttpResponseRedirect(reverse('index', ))
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
    context = {'bbs': bbs, 'rubric': rubric}
    template = get_template('bboard/def_index.html')
    return TemplateResponse(request, template, context)


def detail(request, bb_id):
    bb = get_object_or_404(Bb, pk=bb_id)
    return HttpResponse("... Good")


def indexing(request):
    resp_content = ("Здесь будет", "главная", "страница", "сайта")
    files = r'C:\Users\Erlan\Desktop\Dev\Django3.2\Django3\media\bboard\Y\M\D\bg_xpXcF2U.jpg'
    resp = FileResponse(open(files, 'rb'))
    return resp


class TemplateViews(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bboard_obj'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


from django.views.generic.detail import DetailView
from .models import Bb, Rubric


class BbDetailView(DetailView):
    model = Bb
    template_name = 'bboard/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbListView(ListView):
    template_name = 'bboard/by_rubric.html'
    context_object_name = 'bboard_obj'

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BbAddView(FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    initial = {'price': 0.0, "title": 'Mazda RX-8.'}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        self.obj = super().get_form(form_class)
        return self.obj

    def get_success_url(self):
        return reverse('by_rubric', kwargs={'rubric_id': self.obj.cleaned_date['rubric'].pk})


class BbUpdateView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView):
    model = Bb
    queryset = Bb.objects.all()
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context


class BbIndexView(ArchiveIndexView):
    model = Bb
    date_field = 'published'
    date_list_period = 'year'
    template_name = 'bboard/index.html'
    context_object_name = 'bboard'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class YearIndexView(YearArchiveView):
    model = Bb
    template_name = 'bboard/index.html'
    make_object_list = True
    date_field = 'published'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['bboard'] = Bb.objects.all()
        context['rubric'] = Rubric.objects.all()
        return context


class MonthViews(MonthArchiveView):
    model = Bb
    month_format = "%m"
    date_field = 'published'
    template_name = 'bboard/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['bboard'] = Bb.objects.all()
        context['rubric'] = Rubric.objects.all()
        return context


class BbByRubricView(SingleObjectMixin, ListView):
    model = Bb, Rubric
    template_name = 'bboard/by_rubric.html'
    pk_url_kwarg = 'rubric_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Rubric.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BbByRubricView, self).get_context_data(**kwargs)
        context['current_rubric'] = self.object
        context['rubrics'] = Rubric.objects.all()
        context['bboard_obj'] = context['object_list']
        return context

    def get_queryset(self):
        return self.object.bb_set.all()


def index_paginator(request):
    rubric = Rubric.objects.all()
    bboard_obj = Bb.objects.all()
    paginator = Paginator(bboard_obj, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubric, 'page': page, 'bbs': page.object_list}
    return render(request, 'bboard/index.html', context=context)

