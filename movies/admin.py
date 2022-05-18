from django.contrib import admin
from .models import Genre, Movie


# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # tuple of fields


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)  # tuple to exclude fields
    list_display = ('title', 'genre', 'release_year', 'daily_rate', 'release_year')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
