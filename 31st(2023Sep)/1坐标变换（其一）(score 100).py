# input n & m
n,m = map(int,input().split())
sum_dx = 0
sum_dy = 0

# sum up the data
for _ in range(n):
    dx,dy = map(int,input().split())
    sum_dx += dx
    sum_dy += dy
    
# operate
for _ in range(m):
    x,y = map(int,input().split())
    x += sum_dx
    y += sum_dy
    print(x,end = ' ')
    print(y)