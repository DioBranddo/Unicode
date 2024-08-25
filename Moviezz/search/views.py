from django.shortcuts import render
from .models import Movie
import urllib.request
import json

def clean_title(title):
    return title.title().strip()

def titleSearch(request):
    movies = []
    result = ""
    movie1_data = None
    movie2_data = None

    if request.method == 'POST':
        movieTitle = clean_title(request.POST.get('movieTitle', ''))
        tTitle = clean_title(request.POST.get('tTitle', ''))
        movie1 = clean_title(request.POST.get('movie1', ''))  
        movie2 = clean_title(request.POST.get('movie2', ''))

        if movieTitle:
            url = f'http://www.omdbapi.com/?s={movieTitle}&apikey=c88dab6a&page=1'
            with urllib.request.urlopen(url) as response:
                res = response.read()
                json_data = json.loads(res)
                if json_data.get('Response') == "True":
                    movies = json_data.get('Search', [])
                else:
                    movies = []
        
        # Task 3 ---------------------------------------------------
        elif tTitle:
            url = f'http://www.omdbapi.com/?t={tTitle.replace(' ', '\\')}&apikey=c88dab6a&page=1'
            with urllib.request.urlopen(url) as response:
                res = response.read()
                json_data = json.loads(res)
                if json_data.get('Response') == "True":
                    movie_data = json_data 
                    title = clean_title(movie_data.get('Title'))
                    year = movie_data.get('Year', '')
                    genre = movie_data.get('Genre', '')
                    imdbrating = movie_data.get('imdbRating')
                    rated = movie_data.get('Rated')
                    poster = movie_data.get('Poster')

                    movie, created = Movie.objects.get_or_create(
                        title=title,
                        defaults={'year': year if year else None, 'genre': genre, 'poster': poster, 'imdbrating': imdbrating, 'rated': rated, 'searchCount': 1}
                    )

                    if not created:
                        movie.searchCount += 1
                        movie.save()

                    movies = [{'Title': title, 'Year': year, 'Poster': poster}]
        
        #Task 4------------------------------------------------

        if movie1 and movie2:

            movie1_obj, created = Movie.objects.get_or_create(
                title=movie1,
                defaults={'searchCount': 0}
            )
            if not created:
                movie1_data = {
                    'Title': movie1_obj.title,
                    'Year': movie1_obj.year,
                    'Poster': movie1_obj.poster,
                    'SearchCount': movie1_obj.searchCount
                }
            else:
                url = f'http://www.omdbapi.com/?t={movie1.replace(' ', '\\')}&apikey=c88dab6a&page=1'
                with urllib.request.urlopen(url) as response:
                    res = response.read()
                    json_data = json.loads(res)
                    if json_data.get('Response') == "True":
                        movie1_data = {
                            'Title': json_data.get('Title'),
                            'Year': json_data.get('Year'),
                            'Poster': json_data.get('Poster'),
                            'SearchCount': 0
                        }
                        movie1_obj.year = movie1_data['Year']
                        movie1_obj.poster = movie1_data['Poster']
                        movie1_obj.searchCount = 0
                        movie1_obj.save()

            # Fetch or create movie2 data
            movie2_obj, created = Movie.objects.get_or_create(
                title=movie2,
                defaults={'searchCount': 0}
            )
            if not created:
                movie2_data = {
                    'Title': movie2_obj.title,
                    'Year': movie2_obj.year,
                    'Poster': movie2_obj.poster,
                    'SearchCount': movie2_obj.searchCount
                }
            else:
                url = f'http://www.omdbapi.com/?t={movie2.replace(' ', '\\')}&apikey=c88dab6a&page=1'
                with urllib.request.urlopen(url) as response:
                    res = response.read()
                    json_data = json.loads(res)
                    if json_data.get('Response') == "True":
                        movie2_data = {
                            'Title': json_data.get('Title'),
                            'Year': json_data.get('Year'),
                            'Poster': json_data.get('Poster'),
                            'SearchCount': 0
                        }
                        movie2_obj.year = movie2_data['Year']
                        movie2_obj.poster = movie2_data['Poster']
                        movie2_obj.searchCount = 0
                        movie2_obj.save()

            # Compare movie search counts
            if movie1_data and movie2_data:
                if movie1_data['SearchCount'] > movie2_data['SearchCount']:
                    result = f"{movie1_data['Title']} is more popular than {movie2_data['Title']}."
                elif movie1_data['SearchCount'] < movie2_data['SearchCount']:
                    result = f"{movie2_data['Title']} is more popular than {movie1_data['Title']}."
                else:
                    result = f"{movie1_data['Title']} and {movie2_data['Title']} have the same popularity."

            return render(request, 'game.html', {'movie1_data': movie1_data, 'movie2_data': movie2_data, 'result': result})
            
    return render(request, 'title.html', {'movies': movies})

def genreSearch(request):
    return render(request, 'genre.html')
