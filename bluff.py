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
            if x == 1:
                sum += 1
        res.append(sum)

    counter = collections.Counter(res)
    probability_list = collections.Counter(res)
    print(counter)

    probability_sum = 0
    for i in range(number_of_cubes, -1, -1):
        probability_list[i] = (probability_list[i]/number_of_experiments)*100 + probability_sum
        probability_sum = probability_list[i]
    return probability_list

if __name__ == "__main__":
    with open('result.txt', 'w') as f:
        for i in range(2, 6):
            a = simulation(i, 6, 10000)
            print('probability of getting * when throw ', i, 'cubes:')
            f.write('probability of getting * when throw ' + str(i) + ' cubes:\n')
            str_to_write = ''
            for g in a.items():
                if g[0] != 0:
                    str_to_write += str(g[0]) + ':' + "{:3.1f}".format(g[1]) + '%; '
            print(str_to_write, '\n')
            f.write(str_to_write + '\n')

            a = simulation(i, 3, 10000)
            print('probability of getting any number plus * when throw ', i, 'cubes:')
            f.write('probability of getting any number plus * when throw ' + str(i) + ' cubes:\n')
            str_to_write = ''
            for g in a.items():
                if g[0] != 0:
                    str_to_write += str(g[0]) + ':' + "{:3.1f}".format(g[1]) + '%; '
            print(str_to_write, '\n')
            f.write(str_to_write + '\n\n')
