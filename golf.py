par = int(input())
strokes = int(input())

if par < 3:
    print('Error')
elif strokes == par:
    print('Par')
elif par - strokes >= 2:
    print('Eagle')
elif par - strokes == 1:
    print('Birdie')
elif strokes > par:
    print('Bogey')
