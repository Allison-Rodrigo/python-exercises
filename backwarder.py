def split(word):
    return[char for char in word]

bk = []

w = split(input())


for i in range(len(w)):
    a = len(w)-i-1
    bk.append(w[a])

b = ''.join(bk)

print(b)
