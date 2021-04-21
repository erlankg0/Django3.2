from django.contrib import admin
from job.models import Blog, Person, Album, Musician, Author, Entry


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "tag_line",
    )
    list_display_links = (
        "name",
        "tag_line",
    )


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "surname",
        "size",
    )
    list_display_links = (
        "pk",
        "name",
        "surname",
        "size",
    )
    search_fields = (
        "pk",
        "name",
        "surname",
        "size",
    )


class AlbumAdmin(admin.ModelAdmin):
    list_display_links = (
        #"artist",
        "name",
        "release_date",
        "nus_star",
    )
    list_display = (
        #"artist",
        "name",
        "release_date",
        "nus_star",
    )
    search_fields = (
       # "artist",
        "name",
        "release_date",
        "nus_star",
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    list_display_links = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )


class MusicianAdmin(admin.ModelAdmin):
    list_display_links = (
        "author",
        "instrument"
    )
    list_display = (
        "author",
        "instrument"
    )
    search_fields = (
        "author",
        "instrument"
    )

"""
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "blog",
        "headline",
        "body_text",
        "pub_date",
        "mod_date",
        "authors",
        "number_of_comments",
        "number_of_pingbacks",
        "rating",
    )
    list_display_links = (
        "blog",
        "headline",
        "body_text",
        "pub_date",
        "mod_date",
        "authors",
        "number_of_comments",
        "number_of_pingbacks",
        "rating",
    )
    search_fields = (
        "blog",
        "headline",
        "body_text",
        "pub_date",
        "mod_date",
        "authors",
        "number_of_comments",
        "number_of_pingbacks",
        "rating",
    )
    list_filter = (
        "blog",
        "headline",
        "body_text",
        "pub_date",
        "mod_date",
        "authors",
        "number_of_comments",
        "number_of_pingbacks",
        "rating",
    )"""


admin.site.register(Blog, BlogAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Entry)
