import csv

from pathlib import Path


def ratings_field(element):
    return element[2]


def sort_movies(movies_list):
    movies_list.sort(key=ratings_field, reverse=True)


def agr_movies(movies):
    result = {}
    for movie in movies:
        res = result.get(movie[1], [0, 0.0])
        res[0] += 1
        res[1] += float(movie[2])
        result[movie[1]] = res
    return result


all_movies = []
path = Path('IMDB-Movie-Data.csv')
if path.is_file():
    with open(path, 'r') as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            all_movies.append([row["Title"], row["Year"], row["Rating"]])
else:
    print("EXCEPTION!")

# top 250
sort_movies(all_movies)
with open('top250_movies.csv', 'w') as top250:
    writer = csv.writer(top250)
    for row in all_movies[:250]:
        writer.writerow([row[0]])

# write aggregations
agg_movies = {}
for k, v in agr_movies(all_movies).items():
    agg_movies[k] = v[1] / v[0]
with open('ratings.csv', 'w') as aggregated:
    writer = csv.writer(aggregated)
    for k, v in agg_movies.items():
        writer.writerow([k, v])
