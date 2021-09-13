sum = list(map(int,input().split()))
count = 0
for i in range(len(sum)):
    count = count+sum[i]
print("sum : ",count)