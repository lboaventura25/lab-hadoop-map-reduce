#!/usr/bin/python3
import sys


class UserRating:
    def __init__(self, rating):
        self.user_id = rating[0]
        self.movie_id = rating[1]
        self.rating = rating[2]
        self.ts = rating[3].split('\n')[0]

    def __str__(self):
        return f'{self.user_id}\t{self.movie_id}\t{self.rating}\t{self.ts}'
        # return f'USER: {self.user_id}, MOVIE: {self.movie_id}, RATING: {self.rating}, TS: {self.ts}'


mapper_input = sys.stdin.readlines()

for linha in mapper_input[1::]:
    linha = linha.strip()
    linha = linha.split(',')
    user_rating = UserRating(linha)

    print(user_rating)
