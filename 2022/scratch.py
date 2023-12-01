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


import heapq
def test_priorityqueue():
    customers = []
    heapq.heappush(customers, (2, "Harry"))
    heapq.heappush(customers, (3, "Charles"))
    heapq.heappush(customers, (1, "Riya"))
    heapq.heappush(customers, (4, "Stacy"))
    heapq.heapreplace(customers, (2, "Harry"), (4, "Harry"))
    while customers:
        x = heapq.heappop(customers)
        print(x[1])

from queue import PriorityQueue

def test_priorityqueue2():
    pq = PriorityQueue()
    pq.put((3, 'Test'))
    pq.put((1, 'ABC'))
    pq.put((2, 'DEC'))

    pq.put((3,'DEC'))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        print(current_vertex)


print(ord('a')) # 7
print(ord('b')) # 8
print(ord('c')) # 9


# a -> c = valid -2, 2
# a -> b = valid -1,1
# c -> a = not valid 2,-2
# c -> b = valid 1, -1