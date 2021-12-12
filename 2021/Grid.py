import numpy as np
# Shape (4,5)
#   0 axis---->
#  1  (0,0) (0,1) (0,2) (0,3) (0,4)  
#  a  (1,0) (1,1) (1,2) (1,3) (1,4) 
#  x  (2,0) (2,1) (2,2) (2,3) (2,4) 
#  |  (3,0) (3,1) (3,2) (3,3) (3,4) 
#  \/
class Grid:
    def __init__(self, array):
        # if shape = x then 2darray else 3darray
        self.grid2d = np.array(array)
        shape = self.grid2d.shape
        self.num_rows = shape[0]
        self.num_columns = shape[1]

    def get_all_adjacent_positions(self, row, col):
        adj = []
        if(row > 0):
            adj.append((row - 1, col))
        if(col > 0):
            adj.append((row, col - 1))
        if(row < self.num_rows):
            adj.append((row + 1, col))
        if(col < self.num_columns):
            adj.append((row, col + 1))
    

class TestGrid:
    def __init__(self):
        self.sut = [[1,5,7,9],
                    [4,6,10,2],
                    [3,8,11,0]]
        self.grid = Grid(self.sut)

    def print_all_numbers(self):
        grid2d = self.grid.grid2d
        nums_as_str = ''
        for row, col in np.ndindex(grid2d.shape):
            nums_as_str += str(grid2d[row,col]) + ' '

        print(nums_as_str)


tg = TestGrid()
tg.print_all_numbers()
        
    


