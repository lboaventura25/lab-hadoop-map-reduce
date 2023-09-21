user_ratings = []
grouped_ratings = {}


class UserRating:
    def __init__(self, rating):
        self.user_id = rating[0]
        self.movie_id = rating[1]
        self.rating = rating[2]
        self.ts = rating[3].split('\n')[0]

    def __str__(self):
        return f'USER: {self.user_id}, MOVIE: {self.movie_id}, RATING: {self.rating}, TS: {self.ts}'


def grouped_users_ratings():
    global grouped_ratings, user_ratings

    for user_rating in user_ratings:
        user_id = user_rating.user_id
        movie_id = user_rating.movie_id
        rating = user_rating.rating

        if user_id in grouped_ratings.keys():
            grouped_ratings[user_id].append((movie_id, rating))
        else:
            grouped_ratings[user_id] = [(movie_id, rating)]


def read_file():
    global user_ratings
    movies_file = open('./movies.txt', 'r')
    lines = movies_file.readlines()

    for line in lines[1::]:
        rating = line.split(',')
        user_ratings.append(UserRating(rating))


read_file()
grouped_users_ratings()

for user, movies_ratings in grouped_ratings.items():
    print(f'USER: {user}, MOVIES_RATINGS: {movies_ratings}')
