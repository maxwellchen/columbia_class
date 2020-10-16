#Question 20

dicter = {}
for value in range(2, 100):
    if value % 7 == 0 or value % 17 == 0:
        dicter[value] = True
