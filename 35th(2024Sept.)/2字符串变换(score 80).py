# input string & n (as the number of rules)
s = input()
n = int(input())

# set up a dictionary to save rules (including char 1 & 2)
trans_rule = {}
for j in range(n):
    rule = input().strip()[1:-1]
    char_1 = rule[0]
    char_2 = rule[1]
    trans_rule[char_1] = char_2

# input m (as the number of k) &k (as the number of the transforming times)
m = int(input())
arr = list(map(int,input().split()))

# save every result in history
history = {}

# calculate every result of k
def transform(s,k):
    if k in history:
        return history[k]

    tran_s = s
    # apply the rule
    for _ in range(k):
        new_s = ''.join(trans_rule.get(i,i) for i in tran_s)

        # check whether in a repeated cycle
        if new_s == tran_s:
            break

        tran_s = new_s

    #store the result in history
    history[k] = tran_s
    return tran_s

# print every answer
for k in arr:
    tran_s = transform(s,k)
    print(tran_s)