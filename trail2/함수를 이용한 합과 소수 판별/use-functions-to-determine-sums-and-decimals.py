a, b = map(int, input().split())

# Please write your code here.

def is_right(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True
def is_even(n):
    str_n = str(n)
    sum = 0
    for i in str_n:
        sum+=int(i)
    if sum%2==0:
        return True
    return False

count = 0
for n in range(a, b+1):
    if is_right(n) and is_even(n):
        count+=1
print(count)