n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def function(A, m):
    sum = 0
    while m>=1:
        sum+=A[m-1]
        if m%2==1:
            m-=1
        else:
            m//=2
    return sum

print(function(A,m))