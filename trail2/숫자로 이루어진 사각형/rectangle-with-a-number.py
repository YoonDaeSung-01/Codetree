n = int(input())

# Please write your code here.
for i in range(n):
    row_numbers = [((i * n + j )% 9) +1 for j in range(n)]
    print(*row_numbers)