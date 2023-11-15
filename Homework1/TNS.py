# Luke Scott
# COSC 311
# Homework 1 - Question 1
# Dr. Wang


def generate_triangular_sequence(triangular_sequence):
    temp = 0
    for i in range(20):
        if (i == 0):
            continue
        temp += i
        triangular_sequence.append(temp)
    print(triangular_sequence)
    
def print_odd(triangular_sequence):
    sum_odd = 0
    for i in triangular_sequence:
        if (i % 2 != 0):
            sum_odd += i
    print("Sum of Odd Integers in the triangular sequence = ", sum_odd)       
    
def print_even(triangular_sequence):
    sum_even = 0
    for i in triangular_sequence:
        if (i % 2 == 0):
            sum_even += i
    print("Sum of Even Integers in the triangular sequence = ", sum_even)
    

triangular_sequence = list()
generate_triangular_sequence(triangular_sequence)
print_odd(triangular_sequence)
print_even(triangular_sequence)
