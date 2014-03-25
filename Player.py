import pygame

class Player(pygame.sprite.Sprite):
    '''
    Model for the Player character.
    
    Can move, jump, attack.
    Has an image, health, rect-bounds.
    '''
    BASE_HEALTH = 10
    BASE_MOVE_SPEED = 1

    def __init__(self, color, width, height):
        '''
        For now, pass in a color, width and height, and
        a block will be created from the given params.
        '''
        # ------------------------------------------------
        # Call super constructor, set image and rect
        # ------------------------------------------------
        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        # In the future this will be an image.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        # ------------------------------------------------
        # Initialize player-specific variables
        # ------------------------------------------------
        self.health = Player.BASE_HEALTH
        self.move_speed = Player.BASE_MOVE_SPEED
        