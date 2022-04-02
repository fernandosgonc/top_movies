from domain.movie import Movie
import rest_controllers.top_250_movies_controller
import service.top_250_movies_service

controller = rest_controllers.top_250_movies_controller.Top250MoviesController()
top_movies_json = controller.get_top_movies()

service = service.top_250_movies_service.Top250MoviesService()
movies_list_json = service.extract_movies_list_from_json(top_movies_json)

movies_list = []
for movie in movies_list_json:
    id = movie['id']
    rank = movie['rank']
    title = movie['title']
    full_title = movie['fullTitle']
    year = movie['year']
    url_image = movie['image']
    crew = movie['crew']
    rating = movie['imDbRating']
    rating_count = movie['imDbRatingCount']

    movie_aux = Movie(id, title, full_title, year, rank,
                      crew, url_image, rating, rating_count)
    movies_list.append(movie_aux)

print(type(movies_list_json[0]))
print(type(movies_list[0]))
print(movies_list[1])
print(movies_list[249])
