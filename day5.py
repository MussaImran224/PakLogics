#day 5
#Practise problem 1 sum of a list
print("Enter the size of list")
size=int(input())
list=[]
total_sum = 0
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list.append(element)
print(list)
for number in list:
     total_sum =total_sum + number
print("The sum of the list:", total_sum)
#problem 2 Reverse List
print("Enter the size of list")
size=int(input())
list=[]
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list.append(element)
print(list)
for i in range(size - 1, -1, -1):
    print(list[i], end=" ")
#problem 3 Second Largest
print("Enter the size of list")
size=int(input())
list=[]
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list.append(element)
print(list)
max1 = max2 = float('-inf')
for n in list:
    if n > max1:
        max2 = max1  
        max1 = n     
    elif n > max2 and n != max1:
        max2 = n  
print(max2)
# problem 4 remove Duplicates
# print("Enter the size of list")
# size=int(input())
# list=[]
# for i in range(size):
#      element = int(input(f"Enter element {i + 1}: "))
#      list.append(element)
# print(list)
# for n in list:
#problem 5 count occurences
print("Enter the size of list")
size=int(input())
list=[]
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list.append(element)
print(list)
print("Enter number to read occurences")
x=int(input())
print(list.count(x))
count=0
for j in list:
     if j==x:
        count=count+1
print(count)
#problem 6 merge and sort
print("Enter the size of list")
size=int(input())
list=[]
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list.append(element)
print(list)
print("Enter the size of list 2")
size=int(input())
list2=[]
for i in range(size):
     element = int(input(f"Enter element {i + 1}: "))
     list2.append(element)
print(list2)

list.extend(list2)
list.sort()
print(list)
#problem 7 word frequency
print("Enter a sentence")
sentence=input()
freq = {}
words = sentence.lower().split()

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
#problem 8 most frequent word
print("Enter a sentence")
sentence=input()
freq = {}
words = sentence.lower().split()

for word in words:
    freq[word] = freq.get(word, 0) + 1
most_frequent = max(freq, key=freq.get)
print(most_frequent)
#problem 9 set intersection
set1={1, 2 , 3, 4, 5}
set2={6, 3 , 9, 1, 2}
print(set1)
print(type(set1))
set3=set1.intersection(set2)
print(set3)
#problem 10 phonebook Lookup
phonebook = {
    "abc": "1234567890",
    "def": "5551234567",
    "ghi": "987-654-3210"
}
name = input("Enter name to look up: ")
if name in phonebook:
    print(phonebook[name])
else:
    print("not found")
#problem 11 Shopping Total