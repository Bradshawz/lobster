import pygame

class Player(pygame.sprite.Sprite):
    """
    Player character.
    
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
        
    """
    Movement
    """
    
    def move_left(self):
        self._move_game_coords(-1 * Player.BASE_MOVE_SPEED, 0)
        
    def move_right(self):
        self._move_game_coords(Player.BASE_MOVE_SPEED, 0)
    
    def move_up(self):
        self._move_game_coords(0, -1 * Player.BASE_MOVE_SPEED)
        
    def move_down(self):
        self._move_game_coords(0, Player.BASE_MOVE_SPEED)
        
    def _move_game_coords(self, x, y):
        """
        Moves the player the specified number of pixels in the
        x and y direction.
        
        y+ is DOWN, x+ is right
        """
        self.rect.x += x
        self.rect.y += y
        
    def _move_math_coords(self, x, y):
        """
        Moves the player the specified number of pixels in the
        x and y direction.
        
        y+ is UP, x+ is right
        """
        self.rect.x += x
        self.rect.y -= y