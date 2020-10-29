while True:

    try:
        a, b, c = input().split()
    except:
        break
    if a == '':
        break

    a=float(a)
    b=float(b)
    c=float(c)
    delta = (b*b)-(4*a*c)

    if delta < 0:
        print('0\n')
    elif delta == 0:
        print('1\n')
    else:
        print('2\n')

