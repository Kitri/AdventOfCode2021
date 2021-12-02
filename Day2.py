def read_file(file_name):
    f = open(file_name)

    lines = []

    with open(file_name, encoding='utf8') as f:
        lines = f.read().splitlines()

    return lines

class Submarine:
  def __init__(self, depth, horizontal_position, aim):
      self.depth = depth
      self.horizontal_position = horizontal_position
      self.aim = aim
    

def apply_instruction_to_submarine(instruction, sub):
    (inst, num) = instruction.split(' ')
    num = int(num)


    if(inst == 'forward'):
        sub.horizontal_position += num
        sub.depth += sub.aim * num
    elif(inst == 'up'):
        sub.aim -= num
    elif(inst == 'down'):
        sub.aim += num

    return sub
    

sub = Submarine(0,0,0)

instructions = read_file('day2.txt')

for instruction in instructions:
    sub = apply_instruction_to_submarine(instruction, sub)

print(f"depth: {sub.depth}")
print(f"position: {sub.horizontal_position}")


print(sub.depth * sub.horizontal_position)
