#loops count from 0 to 100
for i in range(101):
    print(i)
#multiplication table
for i in range(1,11):
    for j in range(1,11):
        print (f"{i}*{j}={i*j}")
#Backwords using loop
for i in range(10,0,-1):
    print(i)
#Even numbers
for i in range(0,10,2):
    print(i)
#SUM numbers
sum=0
for i in range(100,201):
    sum+=i
    print(sum)
 #List using while loop
clist=["canada","usa","mexico"]
i=0
while i<len(clist):
    print(clist[i])
    i+=1

