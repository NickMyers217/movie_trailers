class Movie:
    """This is a class that stores data on movies

    Attributes:
        title               (str): The title of the movie
        poster_image_url    (str): The url for the movies box / poster art
        trailer_youtube_url (str): The youtube url for the movie's trailer
    """
    # Attributes
    title               = ''
    poster_image_url    = ''
    trailer_youtube_url = ''

    # Constructor
    def __init__(self, title, poster, trailer):
        self.title               = title
        self.poster_image_url    = poster
        self.trailer_youtube_url = trailer
