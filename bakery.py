
from math import pi
import statistics


bob_pies = 9 - 3
sally_pies = bob_pies
pies = bob_pies + sally_pies
print("There are",
      + (pies),
      "pies remaining.")

#Assign the values 2 and 0.5 to the radius and height of a cylinder (i.e. a smaller pie).
# Calculate and print the surface area of the cylinder.
#A=2πrh+2πr2
radius = 2
height = 0.5
pi = pi
surface_area = 2*pi*radius*height+2*pi*radius**2


volume = pi * height * (radius**2)

print('The volume of the pie is {0:.2f}.'.format(volume))
print('The surface area of the cylinder is {0:.2f}.'.format(surface_area))

average = [1,2,3,4,5,6,7]
print("The mean number of pies sold is",
    statistics.mean(average))

pie_cost = 2.99
pie_price = 5
days = 7
pie_sales = 6
profit = (pie_price-pie_cost)*days*pie_sales
print("Pie profit = {0:.2f}.".format(profit))