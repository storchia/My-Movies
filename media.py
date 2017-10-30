import webbrowser


class Movie():
    """On this class we will store all movies that will
    appear on the webpage"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_year, movie_director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
        self.director = movie_director
    """Attributes are Movie: Title, Storyline, Poster, Trailer link,
    Release Year, and Director"""
