n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
new_word = sorted(word)
for i in new_word:
    print(i)