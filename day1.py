import math
#Practise problem 1 hello world
print("Hello, Python!\n")
#practise problem 2 echon input
print("Enter a line for me to Read Back")
c=input()
print("The  line you said is\n",c)
#practise problem 3 Add 2 numbers
print("Enter any two integers for me to add")
print("input integer 1")
a=input()
print("input integer 1")
b=input()
sum=int(a)+int(b)
print("The sum is :",sum)
#practise problem 4 Area of Rectangle
print("Enter the width and Height of a Rectangle for me to calculate area")
print("Input Height")
height=float(input())
print("Input width")
width=float(input())
area=height*width
print("The area is :",area)
#Practise Problem 5 Average of three
print("Enter any three integers to calculate average")
a=int(input())
b=int(input())
c=int(input())
average=float((a+b+c)/3)
print("The average is :", average)
#Practise Problem 6 seconds to minutes and seconds
print("Enter seconds")
initial_Seconds=int(input())
minutes=math.floor(initial_Seconds/60)
remaining_Seconds=initial_Seconds%60
print("Minutes are :",minutes)
print("remaining seconds are :",remaining_Seconds)
#Practise Problem 7 celsius to Farenheit
print("Enter temperature in Celsius")
init_Temp=float(input())
farenheit=(init_Temp*9)/(5+32)
print("Temperature in Farenheit is :", farenheit)
#practise problem 8 swap two variables
print("Enter two Variable to Swap")
a=input()
b=input()
a,b=b,a
print("A is ",a,"b is",b)
#practise problem 9 Last digit
print("Enter an integer")
a=input()
b=len(a)
print("Last digit is",a[b-1])
#practise problem 10 Sum of digits(2 digits)
print("Input a two digits integer")
a=input()
b=int(a[0])+int(a[1])
print("The sum is ",b)
#practise problem 11 Simple Interest
print("Enter principal,rate and time")
print("Enter Principal")
principal=float(input())
print("Enter Rate")
rate=float(input())
print("Enter Time")
time=float(input())

interest=(principal*rate*time)/100
print("the interest is :",interest)
#practise problem 12 Format a bill line
print("Enter a string and float")
item=str(input())
price=float(input())
print(f"{item=}")
print(f"{price=}")
# Mini Project
print("Welcome to tip Calculator\nPlease Enter Bill Amount And Percentage you want to tip")
print("Enter Bill Amount")
bill=float(input())
print("Enter Tip Percentage")
tip_Percentage=int(input())
total_Bill=bill+(bill*tip_Percentage/100)
print("Total bill is ",total_Bill)