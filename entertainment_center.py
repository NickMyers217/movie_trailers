import media
import fresh_tomatoes as ft

# An empty list of movies
movies = []

# Create an instance of Movie to hold the data for RoboCop
# and then append it to the list
movies.append(media.Movie(
    'RoboCop',
    'http://ia.media-imdb.com/images/M/MV5BMTk1MDUzMTQ3OV5BMl5BanBnXkFtZTcwMDAwNTk0NA@@._V1_SX640_SY720_.jpg',
    'https://www.youtube.com/watch?v=zbCbwP6ibR4'
))

# Create an instance of Movie to hold the data for First Blood
# and then append it to the list
movies.append(media.Movie(
    'First Blood',
    'http://ia.media-imdb.com/images/M/MV5BNzk5NDc4MDQyNV5BMl5BanBnXkFtZTgwNzg5NTYxMTE@._V1_SX640_SY720_.jpg',
    'https://www.youtube.com/watch?v=IAqLKlxY3Eo'
))

# Create an instance of Movie to hold the data for First Blood
# and then append it to the list
movies.append(media.Movie(
    'Darkman',
    'http://ia.media-imdb.com/images/M/MV5BMTc5MzUxMjk4NF5BMl5BanBnXkFtZTgwNTEzNDk4NjE@._V1_UY1200_CR92,0,630,1200_AL_.jpg',
    'https://www.youtube.com/watch?v=L58rdhCfDIU'
))

# Server a formatted HTML page with the movie data
ft.open_movies_page(movies)
