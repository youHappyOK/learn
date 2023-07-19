def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    elif n <= 0:
        raise TypeError('Bad Oprand n')
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)
move(3, 'a', 'b', 'c')