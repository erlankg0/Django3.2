from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.views.generic.list import ListView

from .forms import BbForm, BBForm
from .models import Bb, Rubric


class Index(TemplateView):
    model = Bb
    queryset = Bb.objects.order_by('title')
    template_name = 'bboard/index.html'
    context_object_name = 'bboard'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['bboard'] = Bb.objects.order_by('title')
        context['rubric'] = Rubric.objects.all()
        return context


class BbCreatView(CreateView):
    template_name = 'bboard/index.html'
    form_class = BBForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['rubric'] = Rubric.objects.all()
        return context


class TemplateViews(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bboard_obj'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


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
    form_class = BBForm
    initial = {'price': 1000.0}

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
    form_class = BBForm
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
