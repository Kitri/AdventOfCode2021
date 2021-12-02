class Submarine:
  def __init__(self, depth, horizontal_position, aim, seafloor_depth = 0):
      self.depth = depth
      self.horizontal_position = horizontal_position
      self.aim = aim
      self.seafloor_depth = seafloor_depth #idk maybe in future?

  # foward, up or down
  #input e.g. forward 1
  def dive(instruction):
    (inst, num) = instruction.split(' ')
    num = int(num)

    if(inst == 'forward'):
        self.horizontal_position += num
        self.depth += sub.aim * num
    elif(inst == 'up'):
        self.aim -= num
    elif(inst == 'down'):
        self.aim += num

  # foward, up or down
  #input e.g. forward 1
  def dive_deprecated(instruction):
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
