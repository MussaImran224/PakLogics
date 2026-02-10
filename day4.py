#day 4
#practise problem 1 sum of first n numbers
print("Enter limit")
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum",sum)
#problem 2 Factorial
print("Enter factorial number")
num=int(input())

if num>0:
    fct = 1
    for i in range(1, num+1):
        fct *= i
    print("Factorial:", fct)
else:
    print("Enter number greater than zero")
#problem 3 Multiplication Table 
print("Enter number")
n=int(input())
for i in range(1,11):
    mul=n*i
    print(n,"*",i,"=",mul)
#problem 4 count digits
print("enter Number")
n=int(input())
count=0
while n>0:
    n=n//10
    count=count+1
print(count)    
#problem 5 sum of digits
print("enter Number")
n=int(input())
sumdigits=0
while n>0:
    digits=n%10
    sumdigits=sumdigits+digits
    n=n//10
print(sumdigits)   
#problem 6 Find Maximum
print("How many numbers")
n = int(input())
print("Enter number")
max_num = int(input())
for i in range(n - 1):
    print("Enter number:")
    num = int(input())
    if num > max_num:
        max_num = num
print("Maximum:", max_num)
#problem 7 Average until 0
sumnum=0
count=0
while True:
    print("enter Number")
    num=int(input())
    if num==0:
        break
    sumnum=sumnum+num
    count=count+1
    if count>0:
        avg=sumnum/count
print("Average is ",avg)
#problem 8 Print a Right Triangle
print("enter Height of triangle")
height=int(input())
for i in range(1,height+1):
    print("*"*i)
#problem 9 FizzBuzz(1..n)
print("Enter Number")
n=int(input())
i=1
for i in range(i,n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
        break
    elif n%5==5:
        print("Buzz")
        break
    elif n%3==0  :
        print("Fizz")
        break
    else:
        print(i)
        break

#problem 10 Prime check
print("Enter number to check prime")
n=int(input())
if n <= 1:
    print(False)
else:
    is_prime = "Prime" 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = "Not Prime"
            break
    print(is_prime)

 #problem 11 List all Divisors
print("Enter Number")
n=int(input())
for i in range(1,n):
    if n%i==0:
        print("Divisor is",i)

#problem 12 Guessing loop
print("Guess The Number")
count=1
correct=7
for i in range(10000):
    print("enter Number")
    guess=int(input())
    if(guess==correct):
        print("Correct Answer")
        break
    count=count+1
print(count)