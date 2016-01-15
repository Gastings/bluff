# -*- coding: utf-8 -*-
__author__ = 'platonov'

import math
n = 5
k = 1
p = (math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))/(6**n)
print(p)