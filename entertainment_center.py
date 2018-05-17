import media
import fresh_tomatoes
toy_story = media.Movie("toy story",
                        "This article is about the original Toy Story film. For the film franchise, see Toy Story (franchise). For the video game, see Toy Story (video game). For other uses, see Toy Story (disambiguation).",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )
avatar = media.Movie("avatar",
                     "avatar",
                     "https://vignette.wikia.nocookie.net/jamescameronsavatar/images/4/40/Avatar2logo.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#toy_story.show_trailer()
School_of_Rock = media.Movie("School of Rock",
                     "https://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg",
                     "https://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")
Maleficent  = media.Movie("Maleficent ",
                     "Maleficent",
                     "http://www.gdedak.com/upload_imgs/video/1495508010-98424-881.jpeg",
                     "https://www.youtube.com/watch?v=w-XO4XiRop0")
Red = media.Movie("Red",
                     "red",
                     "http://www.cinema4tv.com/wp-content/uploads/2017/07/22.jpeg",
                     "https://www.youtube.com/watch?v=-JZ_moituIo")
Despicable_Me = media.Movie("despicable me",
                     "despicable me",
                     "https://www.babonej.com/data/image/723X380/07113665640189201727832838036380.jpg",
                     "https://www.youtube.com/watch?v=sUkZFetWYY0")
movies= [toy_story,avatar,Maleficent ,School_of_Rock,Red ,Despicable_Me]
fresh_tomatoes.open_movies_page(movies)
