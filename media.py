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

    # Constructor
    def __init__(self, title, poster, trailer, year, hero, actor):
        self.title               = title
        self.poster_image_url    = poster
        self.trailer_youtube_url = trailer
        self.year                = year
        self.hero                = hero
        self.actor               = actor
