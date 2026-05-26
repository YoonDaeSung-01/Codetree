n = int(input())

# Please write your code here.

def function(n):
    sum = 0
    for num in str(n):
        sum+=int(num)
    if n%2==0 and sum%5==0:
        print("Yes")
    else:
        print("No")

function(n)
