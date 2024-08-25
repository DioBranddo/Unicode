from django.contrib import admin
from search.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre','imdbrating', 'rated', 'searchCount')
    search_fields = ('title', 'genre')

admin.site.register(Movie, MovieAdmin)