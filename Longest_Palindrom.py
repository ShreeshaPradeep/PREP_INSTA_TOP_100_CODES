a = list(map(int,input().split()))
b=[]
for i in range(len(a)):
    if str(a[i])==str(a[i])[::-1]:
        b.append(a[i])
print(max(b))