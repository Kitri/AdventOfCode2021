import numpy as np
import collections

class Submarine:
  def __init__(self, depth, horizontal_position, aim, seafloor_depth = 0):
      self.depth = depth
      self.horizontal_position = horizontal_position
      self.aim = aim
      self.seafloor_depth = seafloor_depth #idk maybe in future?

  # foward, up or down
  #input e.g. forward 1
  def dive(self, instruction):
    (inst, num) = instruction.split(' ')
    num = int(num)

    if(inst == 'forward'):
        self.horizontal_position += num
        self.depth += self.aim * num
    elif(inst == 'up'):
        self.aim -= num
    elif(inst == 'down'):
        self.aim += num

  # foward, up or down
  #input e.g. forward 1
  def dive_deprecated(self, instruction):
    (inst, num) = instruction.split(' ')
    num = int(num)

    if(inst == 'forward'):
        self.horizontal_position += num
    elif(inst == 'up'):
        self.depth -= num
    elif(inst == 'down'):
        self.depth += num


#input: dataframe containing list of numbers
def sonar_sweep_basic(df):
  depth = "depth"
  prev_depth = "prev_depth"
  df[prev_depth] = df[depth].shift(1)
  df["depth_calculation"] = df[depth] - df[prev_depth]

  return df

#input: dataframe containing list of numbers
def sonar_sweep_sliding_window(df):
  depth = "depth"
  prev_depth= f"prev_{depth}"
  prev_prev_depth = f"prev_prev_{depth}"

  df[prev_depth] = df[depth].shift(1)
  df[prev_prev_depth] = df[prev_depth].shift(1)
  df["depth_sum"] = df[depth] + df[prev_depth] + df[prev_prev_depth]
  df["prev_depth_sum"] = df["depth_sum"].shift(1)
  df["depth_calculation"] = df["depth_sum"] - df["prev_depth_sum"]
  
  return df
    
    
def calculate_number_of_sea_floor_depth_increases(df):
  diffs = df["depth_calculation"]
      
  return diffs[diffs > 0].count()


def read_diagnostic_report(report):
  return ''
  # 5 digit binary
  # First parameter to check = Power Consumption (gamma * epsilon)
  # Generate 2 new binary numbers - gamma and epsilon rate
  # Gamma: Most common bit in the column

def calculate_power_consumptions(binary_list):

  multidim_list = [list(item) for item in binary_list]
  num_list = np.array(multidim_list)

  gamma = ''
  epsilon = ''

  for i in range(0,len(binary_list[0])):
      (x, y) = get_gamma_epsiolon_for_row(num_list, i)
      gamma += x
      epsilon += y

  print(f"g: {gamma}, e: {epsilon}")

  gamma_decimal = int(gamma,2)
  epsilon_decimal = int(epsilon, 2)

  print(f"g: {gamma_decimal}, e: {epsilon_decimal}")

  return gamma_decimal * epsilon_decimal

def get_gamma_epsiolon_for_row(num_list, column):
  col = num_list[:,column]
  counts = collections.Counter(col)

  a = counts['0']
  b = counts['1']

  if( a < b):
    return ('1','0')
  elif (b < a):
    return ('0','1')
  else:
    return ('1','0')

def calculate_rating(bin_list, common):
  for i in range(0, len(bin_list[0])):
    num_list = np.array([list(item) for item in bin_list])
    (x, y) = get_gamma_epsiolon_for_row(num_list, i)
    col = num_list[:,i]
    i_list = []
    if(common == 'mc'):
      i_list = [i for i, j in enumerate(col) if j == x]
    else:
      i_list = [i for i, j in enumerate(col) if j == y]
    temp_bin_list = [bin_list[i] for i in i_list]
    bin_list = [x for x in temp_bin_list if x in bin_list]
    if(len(bin_list) == 1):
      break

  return bin_list
  

def get_life_support_rating(binary_list):
  multidim_list = [list(item) for item in binary_list]
  num_list = np.array(multidim_list)

  gamma = '000'
  epsilon = '111'

  index_list = [i for i, j in enumerate(binary_list)]

#   new_bin_list = binary_list
# 
#   for i in range(0, len(binary_list[0])):
#     num_list = np.array([list(item) for item in new_bin_list])
#     (x, y) = get_gamma_epsiolon_for_row(num_list, i)
#     col = num_list[:,i]
#     i_list = [i for i, j in enumerate(col) if j == x]
#     temp_bin_list = [new_bin_list[i] for i in i_list]
#     new_bin_list = [x for x in temp_bin_list if x in new_bin_list]
#     print(new_bin_list)
    
  gamma_list = calculate_rating(binary_list, 'mc') # most common
  print(gamma_list)

  gamma = gamma_list[0]

  epsilon_list = calculate_rating(binary_list, 'lc') # most common
  print(epsilon_list)

  epsilon = epsilon_list[0]

    
  # col 1:
#   (x, y) = get_gamma_epsiolon_for_row(num_list, 0)
#   col = num_list[:,0]
#   i_list = [i for i, j in enumerate(col) if j == x]
#   new_bin_list = [binary_list[i] for i in i_list]
#   print(new_bin_list)
# 
#   num_list = np.array([list(item) for item in new_bin_list])
#   (x, y) = get_gamma_epsiolon_for_row(num_list, 1)
#   col = num_list[:,1]
#   i_list = [i for i, j in enumerate(col) if j == x]
#   temp_bin_list = [new_bin_list[i] for i in i_list]
#   new_bin_list = [x for x in temp_bin_list if x in new_bin_list]
#   print(new_bin_list)
# 
#   num_list = np.array([list(item) for item in new_bin_list])
#   (x, y) = get_gamma_epsiolon_for_row(num_list, 2)
#   col = num_list[:,2]
#   i_list = [i for i, j in enumerate(col) if j == x]
#   temp_bin_list = [new_bin_list[i] for i in i_list]
#   new_bin_list = [x for x in temp_bin_list if x in new_bin_list]
#   print(new_bin_list)


  
 # for i in range(0,len(binary_list[0])):
 #     (x, y) = get_gamma_epsiolon_for_row(num_list, i)
 #     gamma += x
 #     epsilon += y

 # index_list = [i for i, j in enumerate(binary_list)]
 # 
 # for (i, num) in enumerate(gamma):
 #   print(num)
 #   col = num_list[:,i]
 #   index_list = get_index_list(col, num, index_list)
 #   l = [binary_list[i] for i in index_list]
 #   print(l)
 #   if(len(index_list) == 1):
 #     break

#   index0 = [i for i, j in enumerate(col) if j == '0']
 #  index1 = [i for i, j in enumerate(col) if j == '1']

  # [print(binary_list[i]) for i in index_list]

    
  oxygen_generator_rating = int(gamma, 2)
  CO2_scrubber_rating = int(epsilon, 2)

  print(oxygen_generator_rating)
  print(CO2_scrubber_rating)

  return oxygen_generator_rating * CO2_scrubber_rating

def get_index_list(col, num, current_indexes):
  # Get indexes for current number
  # E.g. 1 3 5 6
  # E.g. original list = 1 5 7
  # New list = 1 5
  index_list = [i for i, j in enumerate(col) if j == num]

  return [x for x in index_list if x in current_indexes]



  
