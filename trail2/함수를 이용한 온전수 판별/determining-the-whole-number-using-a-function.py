a, b = map(int, input().split())

# Please write your code here.
def is_right(n):
    if n % 2 == 0 or (n%3==0 and n%9!=0) or n%10==5:
        return False
    else:
        return True

count = 0
for i in range(a, b+1):
    if is_right(i):
        count+=1
    
print(count)