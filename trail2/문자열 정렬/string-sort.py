str = input()

# Please write your code here.

str_list = list(str)
str_list.sort()
new_str = "".join(str_list)
print(new_str)