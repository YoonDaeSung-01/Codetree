a, b = map(int, input().split())

# Please write your code here.
def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
sum = 0
for n in range(a, b+1):
    if is_prime(n):
        sum+=n
print(sum)
