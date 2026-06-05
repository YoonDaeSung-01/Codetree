N = int(input())

# Please write your code here.

def print_only(n):
    if n == 0:
        return

    print(n, end = " ")
    print_only(n-1)
    print(n, end = " ")

print_only(N)