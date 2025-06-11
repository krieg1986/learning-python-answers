def countdown(num):
    if num >= 1:
        print(num)
        countdown(num - 1)
    else:
        print('stop')

print(countdown(5))
