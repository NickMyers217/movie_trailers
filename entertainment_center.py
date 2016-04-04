import media
import fresh_tomatoes as ft

# An empty list of movies
movies = []

# Create an instance of Movie to hold the data for RoboCop
# and then append it to the list
movies.append(media.Movie('tt0093870',
                          'https://www.youtube.com/watch?v=zbCbwP6ibR4',
                          'Officer Murphy / RoboCop'))

# Create an instance of Movie to hold the data for First Blood
# and then append it to the list
movies.append(media.Movie('tt0083944',
                          'https://www.youtube.com/watch?v=IAqLKlxY3Eo',
                          'Jonh Rambo'))

# Create an instance of Movie to hold the data for Darkman
# and then append it to the list
movies.append(media.Movie('tt0099365',
                          'https://www.youtube.com/watch?v=L58rdhCfDIU',
                          'Peyton Westlake / Darkman'))

# Serve a formatted HTML page with the movie data
ft.open_movies_page(movies)
