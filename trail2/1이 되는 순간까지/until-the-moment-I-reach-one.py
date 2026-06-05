N = int(input())

# Please write your code here.
def make_one(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return make_one(n // 2) + 1
    else:
        return make_one(n // 3) + 1

print(make_one(N))

    