import pygame
from pygame import Rect

class Player(pygame.sprite.Sprite):
    """
    Model for the Player character.
    
    Can move, jump, attack.
    Has an image, health, rect-bounds.
    """
    BASE_HEALTH = 10
    BASE_MOVE_SPEED = 1

    def __init__(self, image_filename):
        """
        Pass in the filename of the image to represent
        this player.
        """
        # ------------------------------------------------
        # Call super constructor, set image and rect
        # ------------------------------------------------
        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        # ------------------------------------------------
        # Initialize player-specific variables
        # ------------------------------------------------
        self.health = Player.BASE_HEALTH
        self.move_speed = Player.BASE_MOVE_SPEED
    
    def move(self, x, y):
        self.move_game_coords(x, y)
        
    def move_game_coords(self, x, y):
        """
        Moves the player the specified number of pixels in the
        x and y direction.
        
        y+ is DOWN, x+ is right
        """
        self.rect.x += x
        self.rect.y += y
        
    def move_std_coords(self, x, y):
        """
        Moves the player the specified number of pixels in the
        x and y direction.
        
        y+ is UP, x+ is right
        """
        self.rect.x += x
        self.rect.y -= y