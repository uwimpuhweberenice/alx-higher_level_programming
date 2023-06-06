#!/usr/bin/python3
def print_last_digit(number):
    '''prints the last digit of a number'''
    last = abs(number) % 10
    print(f"{last}", end='')
    return last
