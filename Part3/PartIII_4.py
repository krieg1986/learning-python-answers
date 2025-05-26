d = {"a":3, "b":2, "c":1, "d":4}
for k,v in sorted(d.items(), key=lambda item: item[1]):
    print(f"{k}:{v}")

