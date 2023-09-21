#!/usr/bin/python3
import sys
from functools import reduce

reducer_input = sys.stdin.readlines()
reducer_result = {}

for linha in reducer_input:
    linha = linha.strip()
    user_id, movie_id, rating, ts = linha.split('\t')

    if user_id in reducer_result.keys():
        reducer_result[user_id].append((movie_id, rating))
    else:
        reducer_result[user_id] = [(movie_id, rating)]

for user_id, movies in reducer_result.items():
    ratings = reduce(lambda a, b: f'{a} | {b}', movies)
    print(f'{user_id} -> {ratings}')
