a = list(map(int,input().split()))
x = list(dict.fromkeys(a))
for i in x:
    if a.count(i)>1:
        print("duplicate elements are : ",i)
