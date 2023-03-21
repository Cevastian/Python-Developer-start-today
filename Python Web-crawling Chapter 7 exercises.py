'''
print("In normal case.")
no1 = int(input("Please input one number."))
print(no1)


print("\n")


try:
    print("Ocurred exceptional case.")
    no2 = int(input("Please input one number."))
except:
    print("Please input number, not string or special characters.")
    


no1 = 10
no2 = 0
print(no1/no2)



try:
    no1 = 10
    no2 = 0
    print(no1 / no2)
except(ValueError, ZeroDivisionError):
    print("Exceptional case occurred!")
    

no1 = 10
no2 = 0

try:
    print(no1 / no2)
except ZeroDivisionError:
    print("Can't divide by Zero.")
except ValueError:
    print("Input wrong value.")


try:
    no = int(input("Please input number."))
except:
    print("Please input available number.")
else:
    print("Your input number is %s" %no)
    
'''

import os

a_lines = int(input("How many lines do you want to print?"))



f = open("C:\\Users\\chois\\Desktop\\Jupyter codes\\Exception case exercise 001.txt", "r")
txt = f.readlines()
i = 0
try:
    for i in range(a_lines):
        print(txt[i])
except:
    print("All lines were printed.")        
