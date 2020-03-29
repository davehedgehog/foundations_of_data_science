#http://homepages.cs.ncl.ac.uk/jennifer.warrender/teaching/2019-20/csc8621/practicals/csc8621_practical_3.html
#Functions and dictionaries practice

#Task 1
def format(person):
    return "Name:\t" + person['name']

def display(person):
    print(format(person))

person = {'name' :"Harry Potter"}
print(display(person))

#Task 2 - Add height and weight
person['weight'] = 0
person['height'] = 0
print(person)

#Task 3 - create_person function

def create_person (name, height, weight):
    return "Name:\t" + person['name']\
           + ", Height (m): " + person[str('height')]\
           + ", Weight (kg): " + person[str('weight')]

def display(create_person):
    print(format(create_person))

print(format(create_person))

person = {'name':"Harry Potter", 'height': 10, 'weight': 20}
