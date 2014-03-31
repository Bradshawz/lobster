import pygame

class Player(pygame.sprite.Sprite):
    """
    Player character. Subclasses Character->Sprite.
    
    Can move, jump, attack.
    Has an image, health, rect-bounds. 
        
    Has:
    image, rect, mask
    
    Can:
    move itself
    
    Movement is done by "try"ing to move. This does not update the actual
    positions: just the "new" positions. The "move" method must be called every
    frame to update the actual position to the "new" calculated position.
    """
    HORIZONTAL_ACCEL = 1
    VERTICAL_ACCEL = 1
    BASE_HEALTH = 10
    
    def __init__(self, image_filename):
        """
        Pass in the filename of the image to represent
        this player.
        """        
        # Call the parent class (Sprite) constructor)
        super(pygame.sprite.Sprite, self).__init__()
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()
        # Set the collision mask based on the image
        self.mask = pygame.mask.from_surface(self.image)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.new_rect = self.rect
        
        self.vel_x = 0
        self.vel_y = 0
        
        self.on_ground = False
        self.health = self.BASE_HEALTH
        
        
    """
    Movement
    """
    def accel_left(self):
        self.vel_x -= self.HORIZONTAL_ACCEL
    def accel_right(self):
        self.vel_x += self.HORIZONTAL_ACCEL
    def accel_up(self):
        self.vel_y -= self.VERTICAL_ACCEL
    def accel_down(self):
        self.vel_y += self.VERTICAL_ACCEL
    def move_x(self):
        self.rect.x += self.vel_x
    def move_y(self):
        self.rect.y += self.vel_y
    def move(self):
        self.move_x()
        self.move_y()
        
def collide_new_rect(sprite_a, sprite_b):
    return sprite_a.new_rect().colliderect(sprite_b.new_rect())
