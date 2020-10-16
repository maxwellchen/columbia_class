#Question 28

import random
listing = []
counter = 0

while counter < 10000:
    listing.append(random.randint(0, 10))
    counter += 1

listing.sort()
value_counts = {}

for value in listing:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1
