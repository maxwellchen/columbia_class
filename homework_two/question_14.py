#Question 14

listing = []
for value in range(2, 100):
    if value % 3 == 0 or value % 5 == 0:
        listing.append(value)

for value in range(2, 100):
    if value % 3 == 0 and value % 5 == 0:
        listing.remove(value)
