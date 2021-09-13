array = list(map(int,input().split()))
x = []
y = []
for i in range(len(array)//2):
    x.append(array[i])
x.sort()
for j in range(len(array)//2,len(array)):
    y.append(array[j])
y.sort(reverse=True)
print("output : ",*(x+y))