from django.forms import ModelForm
from .models import Bb, Rubric


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ("title", "content", "price", "rubric", "kind")


class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = (
            'name',
        )
