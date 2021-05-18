from django.forms import ModelForm
from .models import Bb, Rubric
from django.forms import modelform_factory, DecimalField
from django.forms.widgets import Select


class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = (
            'name',
        )


BbForm1 = modelform_factory(Bb,
                            fields=('title', 'content', 'price', 'rubric',),
                            labels={'title': 'Название товара',
                                    "content": 'Описание товара', 'price': 'Цена товара'},
                            help_texts={'rubric': 'Не забудьте выбрать рубрику'},
                            field_classes={'price': DecimalField},
                            widgets={'rubric': Select(attrs={'size': 3})}
                            )


class A:
    pass


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'kind', 'price', 'rubric')
        labels = {'title': 'Название товара.'}
        help_texts = {'rubric': 'Объязательно выберите рубрику!'}
        field_classes = {'price': DecimalField}
        widgets = {'rubric': Select({'size': 8})}
