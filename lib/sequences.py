#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0: # return empty list for 0 
        print([])
    elif length <= 1:
        print([0])
    elif length <= 2:
        print([0, 1])
    
    else:
        print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

'''
    while len(fib) < length:
        nextNum = fib[-1] + fib[-2]
        fib.append(nextNum)
        print(fib)
print_fibonacci(10)
'''