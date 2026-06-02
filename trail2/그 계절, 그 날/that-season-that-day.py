Y, M, D = map(int, input().split())

# Please write your code here.
date = {
    "1" : 31,"2" : 28,"3" : 31,"4" : 30,"5" : 31,"6" : 30,
    "7" : 31,"8" : 31,"9" : 30,"10": 31,"11": 30,"12": 31
}
def season(M):
    if 3<=M<=5:
        return "Spring"
    elif 6<=M<=8:
        return "Summer"
    elif 9<=M<=11:
        return "Fall"
    elif M==12 or 1<=M<=2:
        return "Winter"

def is_yoon(y):
    if y % 4 != 0:
        return False
    if y % 100 == 0 and y % 400 != 0:
        return False
    return True

def program(Y,M,D):
    if is_yoon(Y) and M ==2:
        if D<= 29:
            return season(M)
    else:
        if M<13 and D<=date[str(M)]:
            return season(M)
    return -1 
    
print(program(Y,M,D))