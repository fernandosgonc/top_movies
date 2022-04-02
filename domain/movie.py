class Movie:

    def __init__(self, id, title, full_title, year, rank, crew, url_image, rating, rating_count):
        self.__id = id
        self.__title = title
        self.__full_title = full_title
        self.__year = year
        self.__rank = rank
        self._crew = crew
        self.__url_image = url_image
        self.__rating = rating
        self.__rating_count = rating_count

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def full_title(self):
        return self.__full_title

    @property
    def year(self):
        return self.__year

    @property
    def rank(self):
        return self.__rank

    @property
    def crew(self):
        return self.__crew

    @property
    def url_image(self):
        return self.__url_image

    @property
    def rating(self):
        return self.__rating

    @property
    def rating_count(self):
        return self.__rating_count

    def __str__(self):
        info = f'[Title: {self.__title}\nYear:{self.__year}\nRank:{self.__rank}\nRating:{self.__rating}]'
        return info
