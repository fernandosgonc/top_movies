from top_250_movies import create_list_based_on_json_keys, extract_movies_list_from_json, get_top_movies


top_movies = get_top_movies()

movies_list = extract_movies_list_from_json(top_movies)

ids = create_list_based_on_json_keys(movies_list, 'id')
ranks = create_list_based_on_json_keys(movies_list, 'rank')
titles = create_list_based_on_json_keys(movies_list, 'title')
full_titles = create_list_based_on_json_keys(movies_list, 'fullTitle')
years = create_list_based_on_json_keys(movies_list, 'year')
images = create_list_based_on_json_keys(movies_list, 'image')
crew_list = create_list_based_on_json_keys(movies_list, 'crew')
ratings = create_list_based_on_json_keys(movies_list, 'imDbRating')
rating_counts = create_list_based_on_json_keys(movies_list, 'imDbRatingCount')


print(titles)
print(len(titles))
