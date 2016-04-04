# Import the IMDB web API wrapper to request movie data from the internet
import imdb


class Movie:
    """This is a class that stores data on movies

    Attributes:
        title               (str): The title of the movie
        poster_image_url    (str): The url for the movies box / poster art
        trailer_youtube_url (str): The youtube url for the movie's trailer
        year                (str): The year the movie was released
        hero                (str): The name of the movie's hero
        actor               (str): The actor who played the hero
    """
    # Attributes
    title               = ''
    poster_image_url    = ''
    trailer_youtube_url = ''
    year                = ''
    hero                = ''
    actor               = ''

    # the constructor only requires the IMDB movie id, hero, and trailer url
    # The rest of the data can be requested from IMDB
    def __init__(self, imdb_id, trailer, hero):
        # Request the movie's data from IMDB and get back the dict of data
        data = imdb.request_movie(imdb_id)

        # Store all the relevant data in this instance of Movie
        self.trailer_youtube_url = trailer
        self.hero                = hero
        self.title               = data['Title']
        self.poster_image_url    = data['Poster']
        self.year                = data['Year']
        # The lead actor is always first in the list of actors
        self.actor               = data['Actors'][0] 
