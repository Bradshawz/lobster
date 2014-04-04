import pygame
from Enemy import Enemy

class Spawner(pygame.sprite.Sprite):
    """
    Spawns a block that spawns enemies. Can pass in a monster pattern
    to spawn monsters at different rates.
    """  
    def __init__(self, image_filename, x, y, enemydict):      
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

        # Dictionary of enemy images
        self.image_dict = {"basic":"images/chef_standing.png",
                           "spiky":"images/enemy_tmp.png"}

        self.rect.center = (x, y)

        # Sets spawn times for basic enemies
        self.basic_spawn_time = enemydict["basic"]
        self.basic_spawnnumber = self.basic_spawn_time

        # Sets spawn times for spiky enemies
        self.spiky_spawn_time = enemydict["spiky"]
        self.spiky_spawnnumber = self.spiky_spawn_time

    def spawn(self, enemyGroup):
        if pygame.time.get_ticks()//self.basic_spawnnumber != 0:
            enemy = Enemy(self.image_dict["basic"], 
                          self.rect.x+16, self.rect.y+16, "basic")
            enemy.add(enemyGroup)
            self.basic_spawnnumber += self.basic_spawn_time

        if pygame.time.get_ticks()//self.spiky_spawnnumber != 0:
            enemy = Enemy(self.image_dict["spiky"], 
                          self.rect.x+16, self.rect.y+16, "spiky")
            enemy.add(enemyGroup) 
            self.spiky_spawnnumber += self.spiky_spawn_time
