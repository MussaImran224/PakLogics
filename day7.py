#day 7
#practise problem 1 read and count lines
# with open('file.txt','r') as f:
#     count=0    
#     for x in f:
#         print(x)  
#         count=count+1
# print(count)
#practise problem 2 Count words in file
with open('file.txt','r') as f:
    count=0    
    for x in f:
        content=f.read()
        count=len(content)
print(count)            