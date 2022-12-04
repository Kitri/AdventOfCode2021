import common_functions as common
import file_parser as fp

def contains_all(minA,maxA,minB,maxB):
    if (minA >= minB and maxA <= maxB) or (minB >= minA and maxB <= maxA):
        return True
    else:
        return False

def overlaps(minA,maxA,minB,maxB):
    if maxA < minB or maxB < minA:
        return False
    else:
        return True

def input_function(mode, input_list):
    counter = 0
    for item in input_list:
        a,b = item.split(',')
        minA,maxA = a.split('-')
        minB,maxB = b.split('-')
        print(minA,minB,'-',maxA,maxB)
        minA = int(minA)
        minB = int(minB)
        maxA = int(maxA)
        maxB = int(maxB)
        if mode == 1:
            if contains_all(minA,maxA,minB,maxB):
                counter +=1
        else:
            if overlaps(minA,maxA,minB,maxB):
                counter +=1
    
    return counter

def day4_stuff(mode, input_list):
    parsed = input_function(mode,input_list)
    print(parsed)
    return parsed