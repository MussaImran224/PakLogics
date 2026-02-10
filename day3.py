#day3 
#practise problem 1 positive,negative or zero
print("enter integer")
a=int(input())
if a>0:
    print("Positive")
elif a==0:
    print("Zero")
else:
    print("Negative")
#problem 2 even or odd
print("Enter a number")
a=int(input())
if a%2==0:
    print("Even")
else:
    print("odd")
#problem 3 largest of three numbers
print("Enter three numbers")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("A is Largest")
elif c>b and c>a:
    print("C is Largest")
elif b>c and b>a:
    print("b is Largest")
else:
    print("they are equal")
#problem 4 Leap Year   
print("Enter Year")
year=input()
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("True")
else:
    print("False")
#problem 5 Grade Classifier
print("Enter your Marks")
marks=input()
if marks>=90:
    print("A+")
elif marks<90 and marks>=80:
    print("B")
elif marks<80 and marks>=70:
    print("C")
elif marks<70 and marks>=60:
    print("D")
else:
    print("F")
#Problem 6 Password length check
print("Enter password to check strength")
password=input()
if len(password)>=8:
    print("Strong")
else:
    print("Weak")            
#problem 7 Triangle Validity
print("Enter three sides of a triangle")
a=input()
b=input()
c=input()
if a+b>c or a+c>b or b+c>a:
    print("It can form a triangle")
else:
    print("No Triangle")
#problem 8 Shipping cost
print("Enter Weight")
weight=float(input())
if weight<=1:
    cost=5
    print("cost :",cost)
elif weight<=5:
    cost=10    
    print("cost :",cost)
else:
    cost=20
    print("cost :",cost)
#problem 9 simple calculator
print("Enter first Number")
a=int(input())
print("Enter second Number")
b=int(input())
print("Enter operator (+, -, *, /)")
c=input()
if c=="+":
    sum=a+b
    print("sum is ",sum)
elif c=="-":
    min=a-b
    print("Subtraction is ",min)    
elif c=="*":
    mul=a*b
    print("Multiplication is ",mul)    
elif c=="/":
    div=a/b
    print("division is ",div)
else:
    print("Invalid Operator")
#problem 10 Username Rules
print("Enter Username")
uname=input().strip()        
if len(uname) <=3  and len(uname)<=15 and uname.isalpha():      
    print("True")
else:
    print("False")    
#problem 11 Ticket Price
print("Enter Age")
age=input()
if age <5:
    price=0
    print("Price is",price)
elif age<18 and age>5:
    price=5
    print("Price is",price)
else:
    price=10
    print("Price is",price)
#Problem 12 Contains both Words
print("Enter sentence ")
sentence = input()
key1="cat"
key2="dog"
if key1 and key2 in sentence:
    print("True")
else:
    print("False")
#Mini Project        
print("BMI Calculator")
print("Enter height") 
a=float(input())
print("Enter weight") 
b=float(input())
bmi=b/(a*a)
if bmi<18.5:
    print("Under")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25.0 and bmi<=29.9:
    print("Overweight")
else:
    print("Obese")  
                    