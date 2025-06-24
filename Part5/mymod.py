def countLines(name):
    data = open(name, 'r')
    return len(data.readlines())
def countChars(name):
    return len(open(name).read())
def test(name):
    return countLines(name), countChars(name)
if __name__ == '__main__':
    print(test('mymod.py'))