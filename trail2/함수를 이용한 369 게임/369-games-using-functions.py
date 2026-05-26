a, b = map(int, input().split())

# Please write your code here.

def function1(num):
    for n in str(num):
        if n in ["3","6","9"]:
            return True
    return False

def function(a,b):
    count=0
    for num in range(a,b+1):
        if num%3 ==0 or function1(num):
            count+=1
    return count
        

print(function(a,b))