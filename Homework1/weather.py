# Luke Scott
# COSC 311
# Dr. Wang
# Homework 1

def play_tennis(outlook, humidity, wind):
    if (outlook == 'Overcast'):
        return False
    
    elif (outlook == 'Sunny'):
        if (humidity == 'High'):
            return False
        else:
            return True
        
    else:
        if (wind == 'strong'):
            return False
        else:
            return True

outlook = input("What is the outlook for today? 'Sunny', 'Overcast', or 'Rainy' : ")
humidity = input("What is the humidity for today? 'High' or 'Normal' : ")
wind = input("How windy is it today? 'Strong' or 'Weak' : ")

if (play_tennis(outlook, humidity, wind)):
    print("You can play tennis today.")
    
else:
    print("You cannot play tennis today.")