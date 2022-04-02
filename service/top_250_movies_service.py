class Top250MoviesService:

    # recebe um json e extrai uma lista de dicionários com os dados de cada filme
    def extract_movies_list_from_json(self, dic):

        if len(dic['errorMessage']) != 0:
            print(f"Something went wrong: {dic['errorMessage']}")
            exit()

        return dic['items']


# cria e retorna uma lista com os valores a partir do nome da chave desejada

    def create_list_based_on_json_keys(self, movies_list, key_name):

        aux_list = []

        if len(movies_list) > 0:
            for movie in movies_list:
                if key_name in movie.keys():
                    value = movie[key_name]
                    aux_list.append(value)

        return aux_list
