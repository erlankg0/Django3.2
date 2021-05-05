from django.contrib import admin
from .models import Bb, Rubric, AdvUser


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


class AdvUserAdmin(admin.ModelAdmin):
    list_display_links = (
        "is_activated",
        "user"
    )
    list_display = (
        "is_activated",
        "user"
    )
    list_filter = (
        "is_activated",
        "user"
    )
    search_fields = (
        "is_activated",
        "user"
    )


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(AdvUser, AdvUserAdmin)

# Register your models here.
