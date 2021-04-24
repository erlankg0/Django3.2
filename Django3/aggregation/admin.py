from django.contrib import admin
from .models import Author, Publisher, Book, Store

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)



# Register your models here.
