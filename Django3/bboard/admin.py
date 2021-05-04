from django.contrib import admin
from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display_links = (
        "title",
        'price',
        'published',
        'rubric'
    )
    list_display = (
        "title",
        'price',
        'published',
        'rubric'
    )
    search_fields = (
        "title",
        'price',
        'content',
        "rubric"
    )
    list_filter = (
        "title",
        'price',
        'published',
        "rubric"
    )


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

# Register your models here.
