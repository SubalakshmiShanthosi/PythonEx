#!/usr/bin/python
# -*- coding: utf-8 -*-


def checkPrime(number):

    # prime numbers are greater than 1

    if number > 1:

            # check for factors

        for i in range(2, number):
            if number % i == 0:
                print ("\nNot a prime number\n"+ str(i), 'times', number // i, 'is', number)
                return bool('false')
            
    else:
        return bool('true')
            

num = int(input('Enter a number to check if it is prime or not : '))
result=checkPrime(num)
if result==bool('true'): 
     print("Given number is prime:")
else:
     print("Not prime")

			
