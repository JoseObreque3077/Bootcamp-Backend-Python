from django.contrib import admin

# Register your models here.
from .models import Director, Movie

admin.site.register(Director)
admin.site.register(Movie)
