def getInput(n):
    filename = '../input/{:02d}.txt'.format(n)

    with open(filename) as f:
        return f.read()