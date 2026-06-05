N = int(input())

# Please write your code here.
def make_sum2(n):
    if n < 10:
        return n ** 2
    return make_sum2(n//10) + (n % 10)**2

print(make_sum2(N))