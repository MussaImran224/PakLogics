#Day2
# Practise Problem 1 First and Last Character
print("Enter a string")
string=str(input())
print(string[0],",",string[-1])
#Practise Problem 2 String Length
print("Enter a string")
string=str(input())
print("The length is ",len(string))
#Problem 3 Reverse a String
print("Enter a string")
string=str(input())
print(string[::-1])
#problem 4 count vowels
print("Enter a string")
string = input()
count = 0
vowels = "aeiouAEIOU"
for i in string:
    if i in vowels:
        count += 1

print("Number of vowels:", count)
#problem 5 Title case name
print("Enter first name")
fname=str(input())
print("Enter last name")
lname=str(input())
tname=fname.upper()+lname.upper()
print(tname)
#problem 6 Remove spaces
print("Enter a string")
string = input()
print(string.replace(" ", ""))
#problem 7 replace word
print("Enter sentence ")
sentence = input()
print(sentence)
print("Enter old word you want to replace")
old = input()
print("Enter the new word")
new = input()
result = sentence.replace(old, new)
print("New Sentence :",result)
#problem 8 palindrome check
print("Enter a string")
string=str(input())
string.replace(" ", "")
string.lower()
reverse_String=string[::-1]
if(reverse_String==string):
    print("Palindrome")
else:
    print("Not Palindrome")   
#problem 9 Extraxct domain
print("Enter Email")
email=input()
splitted=email.split("@")
print(splitted[1])
#problem 10 Read Initial
print("Enter full name")
fname=input()
splitted=fname.split(" ")
firstname=splitted[0]
lastname=splitted[1]
initials=firstname[0]+lastname[0]
print(initials)
#problem 11 Find Substring
print("Input Text")
text = input().strip()
print("Input subtext")
sub = input().strip()
index = text.find(sub)
print(index)
#problem 12 
print("Input line")
line = input()
result = line.split(',')
print(result)
#Mini Project
print("Enter Full Name")
fullName=input()
splitted=fullName.split()
fname=splitted[0].lower()
lname=splitted[1].lower()
print("Input Year")
year=str(input())
username=fname+lname+year
print(username)
