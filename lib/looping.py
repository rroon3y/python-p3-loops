#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    squared_list = []

    for num in int_list:
        squared_num = num ** 2
        squared_list.append(squared_num)

    return squared_list
    print(squared_integers([1, 2, 3, 4, 5]))  
    pass

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    pass
