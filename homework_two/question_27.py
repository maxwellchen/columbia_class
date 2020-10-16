#Question 27

import random
listing = []
counter = 0

while counter < 10000:
    listing.append(random.randint(0, 10))
    counter += 1

new_listing = []
for value in listing:
    if value not in new_listing:
        new_listing.append(value)

listing = new_listing
