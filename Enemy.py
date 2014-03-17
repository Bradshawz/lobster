import pygame
import random

class Enemy(pygame.sprite.Sprite):
    """
    Enemy character.
    
    Can move and kill the player.
    Has an image, rect-bounds.
    """
    BASE_MOVE_SPEED = 1

    def __init__(self, image_filename, pos_x, pos_y):
        """
        Pass in the filename of the image to represent
        this enemy.
        """
        # ------------------------------------------------
        # Call super constructor, set image and rect
        # ------------------------------------------------
        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect(center=(pos_x,pos_y))
        
        # ------------------------------------------------
        # Initialize enemy-specific variables
        # ------------------------------------------------
        self.move_speed = Enemy.BASE_MOVE_SPEED
        
    """
    Movement
    """
    
    
    def move_random(self):
        movetype = random.randint(0,3)
        
        if movetype == 0:
            Enemy.move_right(self)
        if movetype == 1:
            Enemy.move_left(self)
        if movetype == 2:
            Enemy.move_up(self)
        if movetype == 3
            Enemy.move_down(self)
            

    def move_left(self):
        self._move_game_coords(-1 * Enemy.BASE_MOVE_SPEED, 0)
        
    def move_right(self):
        self._move_game_coords(Enemy.BASE_MOVE_SPEED, 0)
    
    def move_up(self):
        self._move_game_coords(0, -1 * Enemy.BASE_MOVE_SPEED)
        
    def move_down(self):
        self._move_game_coords(0, Enemy.BASE_MOVE_SPEED)
        
    def _move_game_coords(self, x, y):
        """
        Moves the enemy the specified number of pixels in the
        x and y direction.
        
        y+ is DOWN, x+ is right
        """
        self.rect.x += x
        self.rect.y += y
        
    def _move_math_coords(self, x, y):
        """
        Moves the enemy the specified number of pixels in the
        x and y direction.
        
        y+ is UP, x+ is right
        """
        self.rect.x += x
        self.rect.y -= y
