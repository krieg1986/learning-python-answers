S = 'happy'
for x in S:
    print(ord(x))

sum = 0
for x in S:
    sum += ord(x)
print("\n")
print(sum)

l  = []
for x in S:
    l.append(ord(x))
print(l)