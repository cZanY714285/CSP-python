# input n,p = row & m,q = column
n,m,p,q = map(int,input().split())
arr = []

# save every element in a list (called 'arr') row by row
for i in range(n):
    every_row = list(map(str,input().split()))
    arr.extend(every_row)

# output every element in 'arr' row by row
for i in range(p):
    result_row = arr[i * q:(i + 1) * q]
    print(' '.join(map(str, result_row)))
