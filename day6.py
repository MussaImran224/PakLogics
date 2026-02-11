#day6
#practise problem 1 Function(absolute Value)
def absolute_value():
    print("Enter value")
    val=int(input())
    print("Value is",val)
    if(val<0):
        abs_val=val*-1
        print("Absolute Value is",abs_val)
    else:
        print("already absolute")    
absolute_value()
#Problem 2 Function Clamp
def clamp(x):
    lo=int(10)
    hi=int(50)
    if x>lo and x<hi:
        return True
    else:
        return False
print(clamp(23))    
#problem 3 Count vowels
def count_Vowel():
    print("enter word")
    n=input()
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for letter in n:
        if letter in vowels:
            count += 1
    print(count)
count_Vowel()
# problem 4 Function is_prime
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
print(is_prime(6))
#Problem 5 Funtion Factorial
def factor(num):
    if num>0:
        fct = 1
        for i in range(1, num+1):
            fct *= i
        return fct
    else:
        return False
print(factor(5))
#problem 6 Random Number Game
import random
def random_number_game():
    secret = random.randint(1, 10)
    guess = None
    print("Random Number Game")
    print("think of a number between 1 and 10.")
    while guess != secret:
        guess = int(input("guess the number"))
        if guess == secret:
            print("You guessed the number")
        else:
            print("try again")
random_number_game()
#problem 7 safe integer Input
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
number = input_int("Enter a value: ")
print("You entered:", number)
#problem 8 Calculator as function
print("welcome to Calculator")
print("Enter two Numbers")
a=int(input())
b=int(input())
print("Enter the operation you want to perform(+,-,*,/)")
oper=input()
def addition():
    sum=a+b
    print(sum)
def subtraction():
    sub=a-b
    print(sub)
def multiplication():
    mul=a*b
    print(mul)
def division():
    div=a/b
    print(div)
if oper=="+":
    print("The sum is:")
    addition()
elif oper=="-":
    print("The subtraction is:")
    subtraction()
elif oper=="*":
    print("The Multiplication is:")
    multiplication()
elif oper=="/":
    print("The Division is:")
    division()
else:
    print("Invalid Operator")    
#problem 9 Distance Between Points
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
print(distance(5,6,7,8))
#problem 10 List Stats Function
def stats():
    
    print("Enter the size of list")
    size=int(input())
    lst=[]
    for i in range(size):
        element = int(input(f"Enter element {i + 1}: "))
        lst.append(element)
    if not lst: 
        return None
    
    minimum = min(lst)
    maximum = max(lst)
    average = sum(lst) / len(lst)
    
    print(minimum, maximum, average)
stats()
#problem 11 Temperature Converter Module
def temp_convert():
    print("Which to convert celsius or farenheit")
    direction=input()
    if direction=="celsius" or direction=="Celsius":
        print("Enter your temperature in celsius")
        init_temp=float(input())
        farenheit=(init_temp*1.8)+32
        print("Temperature in Farenheit is:",farenheit)
    elif direction=="farenheit" or direction=="Farenheit":
        print("Enter your temperature in Farenheit")
        faren_temp=float(input())
        celsius=(faren_temp-32)*(5/9)
        print("Temperature in celsius is:",celsius)
    else:
        print("Invalid Input")
temp_convert()
#problem 12 Handle Bad Input
def age_input():
    try:
        age = int(input("Enter age "))
        if 1 <= age <= 100:
            print("You entered:", age)
        else:
            print("Age must be between 1 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
age_input()
#Mini Project
def farenheit_conversion():
     print("Enter your temperature in Farenheit")
     faren_temp=float(input())
     celsius=(faren_temp-32)*(5/9)
     print("Temperature in celsius is:",celsius)
def celsius_conversion():
    print("Enter your temperature in celsius")
    init_temp=float(input())
    farenheit=(init_temp*1.8)+32
    print("Temperature in Farenheit is:",farenheit)
def meter_conversion():
     print("Enter your length in meter")
     init_length=float(input())
     kilometer=init_length/1000
     print("Length in kiloMeter is:",kilometer)
def kilometer_conversion():
     print("Enter your length in kilometer")
     init_length=float(input())
     meter=init_length*1000
     print("Length in Meter is:",meter)     
print("What do you want to convert length or temperature")
conver=input().lower()
if conver=="length":
    print("Which conversion meter or kilometer")
    lenth=input().lower()
    if lenth=="meter":
        meter_conversion()
    elif lenth=="kilometer":
        kilometer_conversion()
    else:
        print("invalid")    
elif conver=="temperature":
    print("which converion farenheit or celsius")
    temp=input().lower()
    if temp=="farenheit":
        farenheit_conversion()
    elif temp=="celsius":
        celsius_conversion()
    else:
        print("invalid")
else:
        print("invalid")

        