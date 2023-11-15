# Luke Scott
# COSC 311
# Dr. Wang
# Homework 1

from random import randint

def calculate(times, total):
    return float((times / total)*100)

def roll(times_to_roll):
    
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

    for i in range(times_to_roll):
        total = (randint(1,6) + randint(1,6))-2
        rolls[total] += 1
    
    for i in range(11):     
        percent = calculate(rolls[i], times_to_roll)
        print("The percentage of", i+2, "'s rolled is %", format(percent, '.2f'))
            
n = int(input("Enter how many times you would like to roll the dice : "))
roll(n)
