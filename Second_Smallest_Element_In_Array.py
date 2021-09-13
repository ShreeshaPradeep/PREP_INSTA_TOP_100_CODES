x = list(map(int, input("Enter a multiple value: ").split()))
x = list(set(x))
x.sort()
print("sec min :",x[1])