from itertools import pairwise
def funkX():
    return 'dummy'

def funcY(num):
    return num

def funky(*funcs):
    # listy[len(*listy)-1:4] = 'x'
    functions = list(*funcs)
    funcs_len = len(*funcs)

    xx = functions + [lambda: funkX()] * (4 - funcs_len)
    print(xx)


# funky(['a','a'])
# funky([lambda: funcY('x'), lambda: funcY('y')])

def test_iter():
    x =['a','b','c']
    x_iter = iter(x)

    a = next(x_iter,None)
    while a != None:
        b = next(x_iter,None)
        if b == None:
            break
        print(a, b)
        a = b

def test_loop_2_items():
    x =['a','b','c']
    y = pairwise(x)
    for a,b in y:
        print(a,b)

test_loop_2_items()

