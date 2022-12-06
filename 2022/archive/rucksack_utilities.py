
# ASCII a = 97; A = 65
# Priority a = 1; A = 27
# 97-1 = 96; 65 - 27 = 38
def get_priority(letter: chr) -> int:
    priority = (ord(letter) - 38) if letter.isupper() else (ord(letter) - 96)
    return priority;

def split_rucksack_into_2_compartments(rucksack: list) -> list:
    middle_index = int(len(rucksack)/2)
    return [rucksack[:middle_index], rucksack[-middle_index:]]