import random
import datetime

class Video:
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f'{self.name} ({self.year}), views: {self.views}'

class Movie(Video):
    pass

class Series(Video):
    def __init__(self, name, year, genre, season, episode):
        super().__init__(name, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.name} S{str(self.season).zfill(2)}E{str(self.episode).zfill(2)}, views: {self.views}'


library = []

def add_to_library(video):
    library.append(video)

def get_movies():
    return sorted([x for x in library if isinstance(x, Movie)], key=lambda x: x.name)

def get_series():
    return sorted([x for x in library if isinstance(x, Series)], key=lambda x: x.name)

def search_by_name(name):
    result = [x for x in library if x.name.lower() == name.lower()]
    if result:
        return result
    else:
        return f'No videos found with name "{name}"'
      

def add_complete_season(name, year, genre, season_number, num_episodes):
    for episode in range(1, num_episodes + 1):
        series = Series(name, year, genre, season_number, episode)
        add_to_library(series)
add_complete_season("The Simpsons", 1989, "Animation", 1, 25)

def get_episodes_count(series_name):
    count = 0
    series_exist = False
    for video in library:
        if isinstance(video, Series) and video.name.lower() == series_name.lower():
            series_exist = True
            count += 1
    if series_exist:
        return count
    else:
        return f"The series {series_name} doesn't exist in the library"
print(get_episodes_count("The Simpsons"))

def generate_views():
    video = random.choice(library)
    video.views += random.randint(1, 100)

def generate_views_multiple(n):
    for _ in range(n):
        generate_views()

def top_titles(n, content_type='All'):
    if content_type.lower() == "all":
        results = sorted(library, key=lambda x: x.views, reverse=True)[:n]
    elif content_type.lower() == "movies":
        results = sorted([x for x in library if isinstance(x, Movie)], key=lambda x: x.views, reverse=True)[:n]
    elif content_type.lower() == "series":
        results = sorted([x for x in library if isinstance(x, Series)], key=lambda x: x.views, reverse=True)[:n]
    return results
  
top_titles_list = top_titles(3)
for video in top_titles_list:
    print(video)

# Example usage
movie1 = Movie("Pulp Fiction", 1994, "Crime")
movie2 = Movie("The Shawshank Redemption", 1994, "Drama")
movie3 = Movie("The Godfather", 1972, "Crime")
series1 = Series("The Simpsons", 1989, "Animation", 1, 5)
series2 = Series("Game of Thrones", 2011, "Fantasy", 7, 2)
series3 = Series("Breaking Bad", 2008, "Crime", 1, 1)

add_to_library(movie1)
add_to_library(movie2)
add_to_library(movie3)
add_to_library(series1)
add_to_library(series2)
add_to_library(series3)

movie1.play()
movie2.play()
movie3.play()
series1.play()
series2.play()
series3.play()

movies = get_movies()
print("Movies: ")
for movie in movies:
    print(movie)

series = get_series()
print("Series: ")
for serie in series:
    print(serie)

top_titles = top_titles(3, "movies")
print("The Filmoteca")
generate_views_multiple(1000)
current_date = datetime.datetime.now().strftime("%d.%m.%Y")
print(f'Most popular movies and series of the day {current_date}: ' + ', '.join(str(x) for x in top_titles))
