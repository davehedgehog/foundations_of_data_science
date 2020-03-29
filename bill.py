# http://homepages.cs.ncl.ac.uk/jennifer.warrender/teaching/2019-20/csc8621/practicals/csc8621_practical_4.html
# Calculate the bill for a mobile company
# Task 1 - print tariffs

TARIFFS = {1:[20, 200, 150],
           2:[35, 400, 350]}

EXTRA_MINS_RATE = 0.10
EXTRA_TEXT_RATE = 0.05

def available_tariffs():
    out = "{:8} {:9} {:7} {:5}"
    print(out.format("Tariff #", "Flat Rate", "Minutes", "Texts"))
    for tariff in TARIFFS.keys():
        inclusive = TARIFFS[tariff]
        print(out.format(tariff, inclusive[0], inclusive[1],
                         inclusive[2]))
    print()

tariffs_available = available_tariffs()
print(tariffs_available)

#Task 2 - function to calc extra mins/texts and costs
