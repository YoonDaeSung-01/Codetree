M, D = map(int, input().split())

# Please write your code here.

date = {
    "1" : 31,"2" : 28,"3" : 31,"4" : 30,"5" : 31,"6" : 30,
    "7" : 31,"8" : 31,"9" : 30,"10": 31,"11": 30,"12": 31
}

def is_date(mon, day):
    if mon<13 and D <= date[str(mon)]:
        return "Yes"
    return "No"

print(is_date(M,D))