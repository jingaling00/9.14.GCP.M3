# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:22:52 2022

@author: jingy
"""
import math

def gauss(x, mu=0, sigma=1):
    """ Calculate Gaussian probability 
    distribution based on x value, mu, and sigma
    """
    return math.e()**1

def isPrime(n):
    if n<=1:
        return 'Error'
    if n>2 and n%2==0:
        return False
    else:
        for i in range(2,n):
            remain = n%i
            if remain == 0:
                return False
                break
            if remain != 0:
                continue
        return True

def divisorGenerator(n):
    divisors = []
    for i in range(1,n+1):
        remain = n%i
        if remain == 0:
            divisors.append(i)
        else:
            continue
    print(*divisors, sep=', ')

def possibleLists(n,k,repetitions=False,):
    # n is the number of objects
    # k is the number of elements in list
    if repetitions == False: 
        lists = math.factorial(n) / math.factorial(n-k) 
    else:
        lists = n**k 
    return int(lists)

def Pi(i,n,function):
    for j in (i,n+1):
        

if __name__ == "__main__":
    print(isPrime(31))
    divisorGenerator(100)
    print(possibleLists(5,3,repetitions=True)) 
    
    
        
    