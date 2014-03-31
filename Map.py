from Block import *
from pygame.sprite import *

class Map:
    """
    Loads a map from a file
    
    Level file specification:
    suffix: .lvl
    format:
    Each line represents a row of height 16 in game.
    Each line consists of integer values separated by spaces.
    The integer values represent the length of the section.
    Sections alternate between "block" and "empty".
    There can be any number of values on a line.
    There should be exactly 32 rows in order to fill the 480px window height
       as well as the ceiling and floor (which are not visible)
    
    The first possible assignable value represents the square just left of the left edge
       of the screen (this square is not visible).
    
    The screen is 640/480 aka 40/30 in 16x16 squares.
    
    A 0 on a line indicates no blocks on that row
    """
    
    def __init__(self, filename="getonmy.lvl", block_filename="block_blue.png"):
        """
        Loads a map from a filename according to the Map filetype specifications.
        """
        self.filename = filename
        self.block_list = []
        
        # Iterate over each row in the map
        cur_x = -16
        cur_y = -16
        level_file = open(self.filename)
        for line in level_file:
            is_block = True
            for length in line.split():
                for i in range(int(length)):
                    if is_block:
                        self.block_list.append(Block(block_filename, x=cur_x, y=cur_y))
                    cur_x += 16
                # Toggle whether next value represents block or space
                is_block = not is_block
            cur_x = -16
            cur_y += 16
        
        
    def get_blocks(self):
        """
        Returns a list of blocks in this map.
        """
        return self.block_list # TODO return something useful
        