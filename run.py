#Practical 2
#http://homepages.cs.ncl.ac.uk/jennifer.warrender/teaching/2019-20/csc8621/practicals/csc8621_practical_2.html
from datetime import datetime

#Task 1
#input file time.txt
times = []

#Task 2- read in times from file
with open("time.txt") as file:
    for l in file:
        times.append(l.strip())

print(times)
print(len(times))

#Task 3 - Find 10 fastest times in order
fastest = sorted(times)
print(fastest[:10])

#Task 4 - list of time in seconds




