#Practical 2
#http://homepages.cs.ncl.ac.uk/jennifer.warrender/teaching/2019-20/csc8621/practicals/csc8621_practical_2.html

#Task 1 - create list
times = []

#Task 2- read in times from file
with open("time.txt") as file:
    for l in file:
        times.append(l.strip())

print(times)
print(len(times))

#Task 3 - Find 10 fastest times in order
fastest = sorted(times)
fastest = (fastest[:10])
print(fastest)

#Task 4 - list of time in seconds
#seconds_per_unit = {"h": 3600, "m": 60, "s": 1}

#def convert_to_seconds(s):
    #return int(s[:-1]) * seconds_per_unit[s[-1]]

#time_s = list(map(convert_to_seconds,times))
#print(time_s)
#fail, not sure why


#Alternative task 4
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

time_in_seconds = list(map(get_sec, times))
print(time_in_seconds)


#Part B
# Task 1 -Calculate the sum total time runners spent running. Print the result in the following format, DD:HH:MM:SS.
total = sum(time_in_seconds)
day = total // (86400)
total = total % (86400)
hour = total // 3600
total %= 3600
minutes = total // 60
total %= 60
seconds = total
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


#Task 2
# Calculate the mean average time taken to run the Great North Run, rounded to the nearest second.
# Print the result in the following format, HH:MM:SS.

from functools import reduce

def add(x,y):
    return x+y

def ave(x):
    tot = reduce(add,x)
    return tot/len(x)

mean = ave(time_in_seconds)
print(mean)

total = mean

hour = total // 3600
total %= 3600
minutes = total // 60
total %= 60
seconds = total
print("h:m:s-> %d:%d:%d" % (hour, minutes, seconds))