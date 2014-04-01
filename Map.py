from Block import *
from pygame.sprite import *

class Map:
    """
    Loads a map from a file
    
    Level file specification
    ------------------------
    Suffix: .lvl
    Format:
    The file will have 30 rows, each consisting of 40 columns.
    The bottom and top row are not visible - they are the floor and
        ceiling that are just out of view.
    The leftmost and rightmost column are not visible - they are the
        left and right edge that is just out of view.
    
    Each character represents one 16x16 "block" in the game.
    
    Important:
        A space represents "no block", or an empty space.
    Characters are as follows:
    (** Define these here and in char_to_filename dict when you add or  ***
     ** modify tiles     
        =    platform
        -    platform that you can jump up through
    """
    char_to_filename = {'=' : 'block_blue.png',
                        '-' : 'block_yellow.png',
                        }
    
    def __init__(self, filename="getonmy.lvl"):
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
            for char in line:
                # if it is not an empty space or newline
                if char not in {' ', '\n'}:
                    # Create the block
                    block = Block(self.char_to_filename[char], x=cur_x, y=cur_y)
                    
                    #===========================================================
                    # Add special functionality based on block type 
                    #===========================================================
                    if char == '-':
                        # Jump through-able platforms
                        block.can_jump_through = True
                    # if char == 'somechar':
                    #    give it some special property
                    #    or initialize it or something
                    #    This is where the enemies and
                    #    players and teleporters and
                    #    whatnot will get initialized.
                    
                    # Add the block to the block_list
                    self.block_list.append(block)
                        
                cur_x += 16
                
            cur_x = -16
            cur_y += 16
        
        
    def get_blocks(self):
        """
        Returns a list of blocks in this map.
        """
        return self.block_list # TODO return something useful
        