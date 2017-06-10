# Import required packages
import requests  # required to handle requests to OMDB API (movie data)
import json  # required to handle API response object
import movie  # required to create movie object as a class of Movie
import site  # required to render website html, css and js


# API key for OMDB API:
apiKey = 'a7ab3c0e'

# Define movies list to store individual movie imdb id and youtube video
# trailer ids
movies = []
guardians = ['tt2015381', '2cv2ueYnKjg']
movies.append(guardians)
avengers = ['tt0848228', 'eOrNdBpGMv8']
movies.append(avengers)
edge = ['tt1631867', 'yUmSVcttXnI']
movies.append(edge)
logan = ['tt2582802', 'Div0iP65aZo']
movies.append(logan)
mummy = ['tt3896198', '2cv2ueYnKjg']
movies.append(mummy)
sicario = ['tt3397884', 'sR0SDT2GeFg']
movies.append(sicario)

# Define movieData to store list of JSON objects representing a movie's data
movieData = []

# Loop through movies list to, get movie data from API and store as an
# element in the movieData list
for movie in movies:
    r = requests.get('http://www.omdbapi.com/?i=%s&apikey=%s' %
                     (movie[0], apiKey))
    movieJSON = r.json()
    movieJSON['Trailer'] = (movie[1])
    movieJSON[
        'Poster'] = 'http://img.omdbapi.com/?i=%s&h=%s&apikey=%s' % (
        movie[0], '480', apiKey)
    movieData.append(Movie(movieJSON['Title'], movieJSON['Poster'],
                           movieJSON['Trailer'], movieJSON['Year'],
                           movieJSON['Rated'], movieJSON['Released'],
                           movieJSON['imdbRating']))

# Pass movieData to the website rendering template
site.open_movies_page(movieData)
