#write a python program to find the sum of natural numbers

limit=int(input("Enter a number indicating limit: "))
sum=0

for i in range(1,limit+1):
    sum+=i

print("Thes sum of natural nummbers upto",limit,"is:",sum)
