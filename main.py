from top_250_movies import get_top_movies, get_top_movies_as_dict

# dicionário 'cru' obtido a partir do json retornado da API
movies_dic = get_top_movies_as_dict()


# imprimindo cada filme na lista da chave 'items'
for movie in movies_dic['items']:
    print(movie)

# verificando o tamanho da lista de filmes
# print(len(movies_dic['items']))
