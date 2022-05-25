def solveit(test):
     for i in range(1000):
        if test(i):
            return i
     for i in range(1000, -1000, -1):
        if test(i):
            return i
