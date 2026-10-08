#!/usr/bin/python3

def minOperations(n):
    
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations