import collections
tin=input()
k=collections.Counter(tin).most_common(1)[0][0]
print(k)
