#Question 24

dicter = {}
primeList = []

for primes in range(2, 100):
    isPrime = True
    for num in range(2, primes):
        if primes % num == 0:
            isPrime = False
    if isPrime:
        primeList.append(primes)


for value in range(0, 100):
    for elem in primeList:
        if value == 0:
            dicter[value] = 0
        elif value == 1:
            dicter[value] = 1
        elif value % elem == 0:
            dicter[value] = int(value / elem)
