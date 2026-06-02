A = input()

# Please write your code here.

def is_palindrome(str):
    if str == str[::-1]:
        print("Yes")
    else:
        print("No")

is_palindrome(A)