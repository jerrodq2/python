# This is my revised code
# to see original, before i tried to shorten the if else statements and time, see below
unsorted = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]

import random
import time
new = []
for index in range(0,100):
    number = round(random.random() *1000)
    new.append(number)

def sort(list):
    start_time = time.time()
    sorted = []
    length = len(list)
    end = length - 1
    for index in range(len(list)/2):
        min = list[0]
        max = list[0]
        for i in range(length):
            if list[i] < min:
                min = list[i]
            elif list[i] > max:
                max = list[i]
        sorted.insert(index, min)
        sorted.insert(end, max)
        end -= 1
        list.remove(min)
        list.remove(max)
        length -=2
    print sorted
    print ("--- %s seconds ---" % (time.time() - start_time))
sort(unsorted)
sort(new)

#This was my original code before I tried to get rid of all of the if else statements
'''unsorted = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]

import random
import time
new = []
for index in range(0,100):
    number = round(random.random() *1000)
    new.append(number)

def sort(list):
    start_time = time.time()
    sorted = []
    length = len(list)
    for index in range(len(list)):
        min = list[0]
        for i in range(length):
            if list[i] < min:
                min = list[i]
        sorted.append(min)
        list.remove(min)
        length -=1
    print sorted
    print ("--- %s seconds ---" % (time.time() - start_time))
sort(unsorted)
sort(new)'''
