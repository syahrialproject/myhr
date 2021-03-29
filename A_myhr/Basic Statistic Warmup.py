# You are given an array of N integers separated by spaces, all in one line.
# Display the following:
# Mean (m): The average of all the integers.
# Median of this array: In case, the number of integers is odd, the middle element; 
# else, the average of the middle two elements.
# Mode: The element(s) which occurs most frequently. If multiple elements satisfy 
# this criteria, display the numerically smallest one.
# Standard Deviation (SD).
# SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5
# where xi is the ith element of the array
# Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated 
# by a space. This might be a new term to some. However, it is an important concept 
# with a simple, formulaic solution. Look it up!

# Link: https://www.hackerrank.com/challenges/stat-warmup
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
import math as m
import statistics as stpy
from scipy import stats

def mean_confidence_interval(length, mean, stdev):
    return 1.96 * (stdev/ m.sqrt(length))

total = int(input())
numbers = list(map(int,input().split()))
#numbers = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

#set statistic value
mean = np.mean(numbers)
median = np.median(numbers)
mode = int(stats.mode(numbers)[0])
stdev = stpy.pstdev(numbers)
confidence_interval = mean_confidence_interval(total, mean, stdev)
min_conf_int = round(mean - confidence_interval, 1)
max_conf_int = round(mean + confidence_interval, 1)

print(round(mean, 1))
print(round(median, 1))
print(mode)
print(round(stdev, 1))
print(f"{min_conf_int} {max_conf_int}")



