array = list(map(int,input().split()))
array.sort()
print("ASC = ",*array,"\nDESC = ",*array[::-1])