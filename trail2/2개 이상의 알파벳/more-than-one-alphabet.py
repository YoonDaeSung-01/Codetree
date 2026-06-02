A = input()

# Please write your code here.

def is_same(A):
    for i in range(len(A)-1):
        if A[i]!= A[i+1]:
            return "Yes"
    return "No"
        
print(is_same(A))