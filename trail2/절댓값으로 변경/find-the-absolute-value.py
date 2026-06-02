n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def make_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

make_abs(arr)

for i in arr:
    print(i, end=" ")