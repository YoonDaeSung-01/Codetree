text = input()
pattern = input()

# Please write your code here.

def function(text, pattern):
    for i in range(len(text)):
        if len(pattern)==1:
            if text[i] == pattern:
                return i
        else:
            if text[i:i+len(pattern)] == pattern:
                return i
    return -1

print(function(text,pattern))