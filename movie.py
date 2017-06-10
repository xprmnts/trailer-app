# Defining the Movie Class
# Creates an instance of a movie with related details


class Movie():

    def __init__(self, movie_title, poster_image, trailer_id,
                 movie_year, movie_rating, movie_release_date, movie_imdb_rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.youtube_id = trailer_id
        self.year = movie_year
        self.rated = movie_rating
        self.released = movie_release_date
        self.rating = movie_imdb_rating
