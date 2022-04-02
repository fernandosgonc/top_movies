import requests


class Top250MoviesController:

    # acessa o arquivo onde a chave está guardada, que não será posto no github
    def __gets_key(self):
        data = open('important_data.txt', 'r')
        api_key = ''
        for line in data:
            line = line.strip().lower()
            if line.startswith('api.key'):
                value_pos = line.find('=')
                api_key = line[value_pos+1:]

        return api_key

    # faz requisição a api dos top 250 filmes do imdb
    def get_top_movies(self):
        request = requests.get(
            f'https://imdb-api.com/en/API/Top250Movies/{self.__gets_key()}')

        if request.status_code == 200:
            return request.json()
        else:
            print(f'Something went wrong, error code: {request.status_code}')
            return
