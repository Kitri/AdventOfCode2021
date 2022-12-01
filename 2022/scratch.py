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
funky([lambda: funcY('x'), lambda: funcY('y')])

