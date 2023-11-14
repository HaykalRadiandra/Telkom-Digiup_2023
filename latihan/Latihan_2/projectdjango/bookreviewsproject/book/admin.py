from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book
from .models import Publisher

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Book)

