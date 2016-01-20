# -*- coding: utf-8 -*-
__author__ = 'platonov'

import math
import random
import collections

n = 5
k = 1
p = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))/(6**n)
print(p)

def simulation(number_of_cubes, number_of_sides_in_cube, number_of_experiments):
    res = []
    for i in range(1, number_of_experiments + 1):
        sum = 0
        for g in range(1, number_of_cubes + 1):
            x = random.randrange(1, number_of_sides_in_cube + 1)
            if x == 6:
                sum += 1
        res.append(sum)

    counter = collections.Counter(res)
    probability_list = collections.Counter(res)
    print(counter)

    probability_sum = 0
    for i in range(number_of_cubes, 0, -1):
        probability_list[i] = (probability_list[i]/number_of_experiments)*100 + probability_sum
        probability_sum = probability_list[i]
    print(probability_list)

if __name__ == "__main__":
    simulation(15, 6, 10000)