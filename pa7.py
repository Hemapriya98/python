cin = input()
d = list(cin)
d[::2], d[1::2] = d[1::2], d[::2]
bin=''.join(d)
print(bin)
