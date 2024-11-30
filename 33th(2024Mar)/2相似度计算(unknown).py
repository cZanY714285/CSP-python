n,m = input().split()
n = int(n)
m = int(m)

article = input().split()
article = [word.lower() for word in article]

passage = input().split()
passage = [word.lower() for word in passage]

meanwhile = set(article) & set(passage)
included = set(article) | set(passage)

#print(f'article = {article}')
#print(f'passage = {passage}')
#print(f'set(article) = {set(article)}')
#print(f'set(passage) = {set(passage)}')
#print(f'meanwhile = {meanwhile}')
#print(f'included = {included}')

print(len(meanwhile))
print(len(included))
