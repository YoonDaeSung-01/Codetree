a, b = map(int, input().split())

# Please write your code here.

def cal(n1, n2):
    if n1 > n2:
        return n1+25, n2*2
    else:
        return n1*2, n2+25


a, b = cal(a, b)
print(a,b)