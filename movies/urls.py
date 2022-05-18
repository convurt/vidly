from django.urls import path
from . import views

# movies/
# movies/1/details

app_name = 'movies' #app name vaiable for url name spaces (movies:detail for example)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]