# Luke Scott
# COSC 311
# Dr. Wang
# Homework 1

def octagon(o):
    for i in range(o*2):
        if (i < o):
            a = ""
            for k in range(o - i):
                a += " "
            for k in range(o + i*2):
                a += "*"
            for k in range(o - i):
                a += " "
            print(a)
        else:
            a = ""
            for k in range(o * 3):
                a += "*"
            print(a)
      
    for i in range(o):
        a = ""
        for k in range(i+1):
            a += " "
        for k in range((o*3) - ((i+1)*2)):
            a += "*"
        for k in range(i+1):
            a += " "
        print(a)
        
    
o = int(input("Enter the size of your octagon : "))
octagon(o)