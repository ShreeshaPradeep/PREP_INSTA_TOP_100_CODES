arr = list(map(int,input().split()))
x  = list(set(arr))
print(arr)
for i in x:
    print("frequency of  is  time(s)",i,arr.count(i))