n = int(input())

# Please write your code here.

def print_1(n):
    if n == 0:
        return
    
    print_1(n-1)
    print(n, end = " ")

def print_2(n):
    if n == 0:
        return

    print(n, end =" ")
    print_2(n-1)
    


print_1(n)
print("")
print_2(n)