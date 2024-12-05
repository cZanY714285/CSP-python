# input n = row & m = column & t =
n,m,t = map(int,input().split())
arr = []

# save every element in a list (called 'arr') row by row
for i in range(n):
    every_row = list(map(int,input().split()))
    arr.extend(every_row)

# the 't' loop
for _ in range(t):
    op,a,b = map(int,input().split())

    if op == 1:     # 重塑矩阵
        # having input a = row & b = column
        # output every element in 'arr' row by row
        for i in range(a):
            result_row = arr[i * b:(i + 1) * b]
            every_row = ' '.join(map(str,result_row))
        n,m = a,b

    elif op == 2:   # 转置矩阵
        re_arr = [0] * (n * m)
        for i in range(n):
            for j in range(m):
                old_index = i * m + j
                new_index = j * n + i
                re_arr[new_index] = arr[old_index]
        arr = re_arr
        n,m = m,n

    else:           # 元素查询
        print(arr[a * m + b])