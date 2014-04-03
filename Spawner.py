import pygame
from Enemy import Enemy

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
        
        self.rect.center = (x, y)
        self.spawnnumber = 3000


    def spawn(self, enemyGroup):
        if pygame.time.get_ticks()//self.spawnnumber != 0:
            enemy = Enemy("enemy_tmp.png", self.rect.x+16, self.rect.y+16) # Create the enemy
            enemy.add(enemyGroup) # Add the enemy Sprite to the Group
            self.spawnnumber += 3000
