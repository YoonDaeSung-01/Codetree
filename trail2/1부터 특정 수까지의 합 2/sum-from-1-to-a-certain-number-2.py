N = int(input())

# Please write your code here.

def make_sum(n):
    if n == 1:
        return 1
    return make_sum(n-1) + n

print(make_sum(N))   