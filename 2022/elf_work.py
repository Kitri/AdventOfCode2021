def contains_all(minA,maxA,minB,maxB):
   return (minA <= minB <= maxB <= maxA) or (minB <= minA <= maxA <= maxB)

def overlaps(minA,maxA,minB,maxB):
    return maxA >= minB and maxB >= minA

def parse_input(item: str) -> tuple:
    a, b = item.split(",")
    minA, maxA = map(int, a.split("-"))
    minB, maxB = map(int, b.split("-"))

    return ((minA,maxA),(minB,maxB))

def determine_work_share(mode, input_list):
    counter = 0
    logic_func = contains_all if mode == 1 else overlaps
    for item in input_list:
        ((minA,maxA),(minB,maxB)) = parse_input(item)

        if logic_func(minA,maxA,minB,maxB):
            counter +=1
    
    return counter