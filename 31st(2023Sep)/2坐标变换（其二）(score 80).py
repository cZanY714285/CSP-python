from math import cos,sin

# input n & m
n,m = map(int,input().split())

# store op & k in arr_op & arr_k
arr_op = []
arr_k = []
for _ in range(n):
    op,k = map(float,input().split())
    arr_op.append(int(op))
    arr_k.append(k)

# execute the operation
for _ in range(m):
    i,j,x,y = map(float,input().split())
    i = int(i) - 1
    j = int(j) - 1

    for l in range(i,j + 1):
        if arr_op[l] == 1:
            x *= arr_k[l]
            y *= arr_k[l]
        else:
            a = cos(arr_k[l])
            b = sin(arr_k[l])
            new_x = x * a - y * b
            new_y = x * b + y * a
            x,y = new_x,new_y

    # output the result
    print('%.3f %.3f' % (x,y))