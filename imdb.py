#
# This module is a very small wrapper around the IMDB web API
#

# Import the urllib2 module so that we can use HTTP requests
import urllib2
# Import the json library to work with JSON data
import json

def request_movie(imdb_id):
    """This function makes an IMDB API request for a specific movie

    Parameters:
        imdb_id (str): The ID of the movie on IMDB. Look for something like 'ttxxxxxxxx' in the url of your movie on IMDB

    Returns:
        A dictionary of JSON data (psst that's what dicts are anyway)
    """

    # Constructing the url for the API request
    # The query string contains two parameters
    #   i = the id of the movie on IMDB
    #   r = the data format (JSON in this case)
    url = 'http://www.omdbapi.com/?i=' + imdb_id + '&r=json'

    # Use the constructed url to actully perform the request and return the JSON
    return json.load(urllib2.urlopen(url))
