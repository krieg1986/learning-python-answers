x = int(input())
if x == 1:
    print("January")
elif x == 2:
    print("February")
elif x == 3:
    print("March")

match x:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")

d = {1:"January", 2:"February", 3:"March"}

l = ["January", "February", "March"]
