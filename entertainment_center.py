import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club", "You don't speak of the Fight Club",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "1999", "David Fincher")
forrest_gump = media.Movie("Forrest Gump", "A story of a man with an IQ of 75",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0",
                           "1994", "Robert Zemeckis")
heroes = media.Movie("Heroes", "Movie of the Soccer World Cup 1986",
                     "http://www.futbol10shop.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/d/v/dvdheroes.jpg",
                     "http://www.youtube.com/watch_popup?v=EUQ8sruv0pQ",
                     "1987", "Tony Maylam")
pulp_fiction = media.Movie("Pulp Fiction", "Masterpiece from Quentin Tarantino",
                           "https://images-na.ssl-images-amazon.com/images/I/51KEdMtQm-L.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                           "1994", "Quentin Tarantino")
oldschool = media.Movie("Old School", "Grownups go back to College",
                        "https://images-na.ssl-images-amazon.com/images/I/51HoMsIST1L.jpg",
                        "https://www.youtube.com/watch?v=VqtymOtKr48",
                        "2003", "Todd Phillips")
back_to_the_future = media.Movie("Back to the Future",
                                 "A story about time travel",
                                 "https://images-na.ssl-images-amazon.com/images/I/51a3mzh6ymL.jpg",
                                 "https://www.youtube.com/watch?v=yosuvf7Unmg",
                                 "1985", "Robert Zemeckis")
"""Attributes are Movie: Title, Storyline, Poster, Trailer link, Release Year,
and Director"""

movies = [fight_club, forrest_gump, heroes, pulp_fiction, oldschool,
          back_to_the_future]
"""movies = list that include the movies selected"""


fresh_tomatoes.open_movies_page(movies)
"""fresh_tomatoes includes fresh_tomatoes.html,
schanges on design can be performed there"""
