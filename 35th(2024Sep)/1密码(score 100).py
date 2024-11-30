# input n (as a total number) & arr (as the whole)
n = int(input())
arr = []

# for every row:a[]
for _ in range(n):
    a = input()
    arr.append(a)

    # check the whole 3 elements
    have_letter = any ('a' <= i <= 'z' or 'A' <= i <= 'Z' for i in a)
    have_number = any ('0' <= i <= '9' for i in a)
    have_special = any(i == '*' or i == '#' for i in a)

    if not (have_letter and have_number and have_special):
        print('0')

    # check the repeated input
    elif any (a.count(i) > 2 for i in a):
        print('1')
    else :
        print('2')


