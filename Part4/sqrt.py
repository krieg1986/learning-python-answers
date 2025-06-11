import math
n_list = [2,4,9,16,25]
new = []
for x in n_list:
    sqrt = math.sqrt(x)
    new.append(sqrt)
print(new)
new = list(map(math.sqrt, n_list))
print(new)
new = [math.sqrt(x) for x in n_list]
print(new)
new = list((math.sqrt(x) for x in n_list))
print(new)