"""
fizz buzz program
"""
from lib.numbers import INT_100, INT_15, INT_5, INT_3, INT_1
from lib.fizzbuzz import FIZZ, BUZZ

def fizzbuzz(num):
    """fizzbuzz"""
    if not num % INT_15:
        return FIZZ + BUZZ
    elif not num % INT_5:
        return BUZZ
    elif not num % INT_3:
        return FIZZ
    else:
        return str(num)

print([fizzbuzz(i + INT_1) for i in range(INT_100)])
