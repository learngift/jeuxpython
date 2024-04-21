# e s = [9, 3, 16, 3, 8, 11, 1, 3]
s = [8, 0, 16, 3, 8, 1, 15, 3]

def r():
    global s
    s = [8, 0, 16, 3, 8, 1, 15, 3]

def p():
    print(f'   {s[6]: 2d} {s[5]: 2d} {s[4]: 2d}')
    print(f'{s[7]: 2d}           {s[3]: 2d}')
    print(f'   {s[0]: 2d} {s[1]: 2d} {s[2]: 2d}')
    print(-(s[0]+s[1]+s[2]+2*s[3]-s[4]-s[5]-s[6]-2*s[7]))

def j(i):
    a=s[i]
    s[i]=0
    while (a > 0):
        i = (i+1) % 8
        s[i] = s[i] + 1
        a = a - 1
    p()

def a0():
    j(0)

def a1():
    j(1)

def a2():
    j(2)

def b6():
    j(6)

def b5():
    j(5)

def b4():
    j(4)

