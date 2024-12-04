# input the n & m
n,m = map(int,input().split())

# set up a list called 'articles'
articles = []

# fill in article (for every row) & words (for every element)
for _ in range(n):    #every row:0:length;1 - (n-1):words
    article = list(map(int,input().split()))
    length = article[0]
    words = article[1:]
    articles.append(words)

# set a word_set; initialize the word_count
word_set = [set() for _ in range(m+1)]
word_count = [0] * (m + 1)

# count
for i in range(n):
    for word in articles[i]:
        word_set[word].add(i)
        word_count[word] += 1

# print the result
for word in range(1,m + 1):
    print(len(word_set[word]),word_count[word])

