# Link: https://www.hackerrank.com/challenges/stat-warmup/problem
# GitHub: https://github.com/vlwdan
# Developer: Daniel Lopes
# Score: 10.0

# Importing libraries
import math as m
import statistics as stpy
from scipy import stats

# Mean confidence interval function
def mean_confidence_interval(length, mean, stdev):
    return 1.96 * (stdev / m.sqrt(length))

# Reading input
size = int(input())
elements = list(map(float, input().split()))

# Getting statistics values
mean = stpy.mean(elements)
median = stpy.median(elements)
mode = int(stats.mode(elements)[0])
stdev = stpy.pstdev(elements)
confidence_interval = mean_confidence_interval(size, mean, stdev)
min_conf = round(mean - confidence_interval, 1)
max_conf = round(mean + confidence_interval, 1)

# Getting the result and showing it on the screen
print(round(mean,1))
print(round(median,1))
print(mode)
print(round(stdev,1))
print("{} {}".format(min_conf, max_conf))
