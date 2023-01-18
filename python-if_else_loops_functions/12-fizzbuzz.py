#!/usr/bin/python3
def fizzbuzz():
    for nbr in range(1, 100 + 1):
        if nbr % 3 == 0 and nbr % 5 == 0:
            msg = "FizzBuzz"
        elif nbr % 3 == 0:
            msg = "Fizz"
        elif nbr % 5 == 0:
            msg = "Buzz"
        else:
            msg = str(nbr)

        print("{}".format(msg), end=" ")
