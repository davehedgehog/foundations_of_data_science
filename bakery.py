#Code for tasks set at
#http://homepages.cs.ncl.ac.uk/jennifer.warrender/teaching/2019-20/csc8621/practicals/csc8621_practical_1.html

from math import pi
import statistics

#Task 1A
bob_pies = 9 - 3
sally_pies = bob_pies
pies = bob_pies + sally_pies
print("There are",
      + (pies),
      "pies remaining.")

#Task 2A and and 1B
#Assign the values 2 and 0.5 to the radius and height of a cylinder (i.e. a smaller pie).
# Calculate and print the surface area of the cylinder.
#A=2πrh+2πr2
radius = 2 #5
height = 0.5 #1
pi = pi
volume = pi * height * (radius**2)
surface_area = 2*pi*radius*height+2*pi*radius**2

print('The volume of the pie is {0:.2f}.'.format(volume))
print('The surface area of the cylinder is {0:.2f}.'.format(surface_area))


#Task 3A
average = [1,2,3,4,5,6,7]
print("The mean number of pies sold is",
    statistics.mean(average))

#Task 4A
pie_cost = 2.99
pie_price = 5
days = 7
pie_sales = 6
profit = (pie_price-pie_cost)*days*pie_sales
print("Pie profit = {0:.2f}.".format(profit))


#Task 2B
song = "\
Sing a song Of sixpence \n\
A pocket full of rye \n\
Four and twenty blackbirds \n\
Baked in a pie.\n\
When the pie was opened \n\
The birds began to sing \n\
Wasn't that a dainty dish \n\
To set before the king?"

#print(song)

#Task 2B alternative method

f = open("sixpence.txt", "r")

for line in f:
    print(line.strip())

f.close()

#Task2B method 3
with open("sixpence.txt") as file:
    sixpence = file.read()
print(sixpence)