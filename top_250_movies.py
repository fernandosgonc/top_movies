import requests
import json

#acessa o arquivo onde a chave está guardada, que não será posto no github
def __gets_key():
    data = open('important_data.txt', 'r')
    api_key = ''
    for line in data:
        line = line.strip()
        if line.startswith('api.key'):
            value_pos = line.find('=')
            api_key = line[value_pos+1:]

    return api_key


def get_top_movies():
    request = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{__gets_key()}')
    # request.json()
    return request.content

def get_top_movies_as_dict():
    dic_movies = json.loads(get_top_movies())
    return dic_movies


