a =list(map(int,input().split()))
even = 0
odd = 0

for i in a:
    if i%2==0:
        even = even+1
    if i%2!=0:
        odd =odd+1
print("even : ",even,"odd ; ",odd)
