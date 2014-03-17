import pygame

class Spawner(pygame.sprite.Sprite):
    """
    Spawns a block that spawns enemies. Can pass in a monster pattern
    to spawn monsters at different rates.
    """  
    def __init__(self, image_filename, x, y):      
        """
        Pass in the filename of the image to represent
        this spawner.
        """
        # ------------------------------------------------
        # Call super constructor, set image and rect
        # ------------------------------------------------
        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()

        # Set the collision mask based on the image
        self.mask = pygame.mask.from_surface(self.image)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
