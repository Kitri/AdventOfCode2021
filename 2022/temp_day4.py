import common_functions as common
import file_parser as fp

def contains_all(minA,maxA,minB,maxB):
    if minA >= minB and maxA <= maxB:
        return True
    elif minB >= minA and maxB <= maxA:
        return True
    else:
        return False

def makesets(min,max) -> set:
    setA = []
    for i in range(min,max+1):
        setA.append(i)

    return set(setA)



def input_function(input_list):
    counter = 0
    counter_sets = 0
    for item in input_list:
        a,b = item.split(',')
        minA,maxA = a.split('-')
        minB,maxB = b.split('-')
        print(minA,minB,'-',maxA,maxB)
        minA = int(minA)
        minB = int(minB)
        maxA = int(maxA)
        maxB = int(maxB)
        if contains_all(minA,maxA,minB,maxB):
            counter +=1
        # setA = makesets(minA,maxA)
        # setB = makesets(minB,maxB)

        # if setA.issubset(setB) or setB.issubset(setA):
        #     counter_sets += 1


    
    return counter


        

def day4_stuff(mode, input_list):
    parsed = input_function(input_list)
    print(parsed)
    return parsed