#Question 29

import random
listing = []
numbers = 10000
counter = 0
counter2 = 0
value_counts = {}
value_ratios = {}

while counter < numbers:
    listing.append(random.randint(0, 10))
    counter += 1

listing.sort()

for value in listing:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

while counter2 < 11:
    value_ratios[counter2] = value_counts[counter2] / numbers
    counter2 += 1
