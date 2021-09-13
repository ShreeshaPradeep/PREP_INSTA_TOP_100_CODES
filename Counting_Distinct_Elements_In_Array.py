b = list(map(int,input().split()))
count =0
for i in b:
    if b.count(i)==1:
        count = count+1
        print("distinct :",i)
print("number of distinct elements are :",count)