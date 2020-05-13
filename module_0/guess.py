#!/usr/bin/env python
# -*- coding: utf-8

import numpy as np

def game_core_binary(number):
    """ Use binary search as find algorithm """

    count = 0
    lower_bound = 0
    upper_bound = 100

    while True:
        count += 1
        guess = lower_bound + (upper_bound - lower_bound) // 2

        if guess == number:
            return count
        if guess > number:
            upper_bound = guess
        elif guess == lower_bound:
            lower_bound += 1
        else:
            lower_bound = guess

def score_game(game_core):
    np.random.seed(1) # fix random seed
    
    count_ls = []
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")


if __name__ == '__main__':
    score_game(game_core_binary)
