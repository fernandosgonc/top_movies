import requests
import json

# acessa o arquivo onde a chave está guardada, que não será posto no github


def __gets_key():
    data = open('important_data.txt', 'r')
    api_key = ''
    for line in data:
        line = line.strip().lower()
        if line.startswith('api.key'):
            value_pos = line.find('=')
            api_key = line[value_pos+1:]

    return api_key


def get_top_movies():
    request = requests.get(
        f'https://imdb-api.com/en/API/Top250Movies/{__gets_key()}')

    if request.status_code == 200:
        return request.json()
    else:
        print(f'Something went wrong, error code: {request.status_code}')
        return
    # request.json()

# método redundante, já que o python já entende o formato json como um dicionário
# def get_top_movies_as_dict(json_str):
#     dic_movies = json.loads(json_str)
#     return dic_movies


def extract_movies_list_from_json(dic):

    if len(dic['errorMessage']) != 0:
        print(f"Something went wrong: {dic['errorMessage']}")
        exit()

    return dic['items']


# cria e retorna uma lista com os valores a partir do nome da chave desejada
def create_list_based_on_json_keys(movies_list, key_name):

    aux_list = []

    if len(movies_list) > 0:
        for movie in movies_list:
            if key_name in movie.keys():
                value = movie[key_name]
                aux_list.append(value)

    return aux_list
