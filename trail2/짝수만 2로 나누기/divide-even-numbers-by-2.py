n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def is_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 ==0:
            arr[i]= arr[i]//2

is_even(arr)
for i in arr:
    print(i,end=" ")