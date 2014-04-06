import pygame
from Enemy import Enemy
from threading import Timer

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
        
        # Set the image of the spawner Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()

        # Set the collision mask based on the image
        self.mask = pygame.mask.from_surface(self.image)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Dictionary of enemy images
        basic_anims_dict = {"walking" : {"filenames" : ["images/chef_standing.png"],
                                         "frames_between" : 100
                                         },
                            "squished" : {"filenames" : ["images/chef_squished_0.png",
                                                         "images/chef_squished_1.png",
                                                         "images/chef_squished_2.png"],
                                          "frames_between" : 8
                                         },
                            "punched" : {"filenames" : ["images/chef_punched_0.png",
                                                        "images/chef_punched_1.png",
                                                        "images/chef_punched_2.png",
                                                        "images/chef_punched_3.png"],
                                         "frames_between" : 8}
                            }
        spiky_anims_dict = {"walking" : {"filenames" : ["images/chef_spiky_standing.png"],
                                         "frames_between" : 100
                                         },
                            "punched" : {"filenames" : ["images/chef_spiky_punched_0.png",
                                                         "images/chef_spiky_punched_1.png",
                                                         "images/chef_spiky_punched_2.png",
                                                         "images/chef_spiky_punched_3.png"],
                                          "frames_between" : 8
                                          },
                            }
        self.anims_dict = {"basic": basic_anims_dict,
                          "spiky": spiky_anims_dict}

        self.rect.center = (x, y)

        # Sets spawn times for basic enemies
        self.basic_spawn_time = enemydict["basic"]
        self.basic_spawnnumber = self.basic_spawn_time

        # Sets spawn times for spiky enemies
        self.spiky_spawn_time = enemydict["spiky"]
        self.spiky_spawnnumber = self.spiky_spawn_time
        self.busy_spawning_spiky = 0
        self.busy_spawning_basic = 0

    def spawn_basic(self, enemyGroup):
        enemy = Enemy(self.anims_dict["basic"], 
                      self.rect.x+16, self.rect.y+16, "basic")
        enemy.add(enemyGroup)
        self.basic_spawnnumber += self.basic_spawn_time
        self.busy_spawning_basic = 0

    def spawn_spiky(self, enemyGroup):
        enemy = Enemy(self.anims_dict["spiky"], 
                      self.rect.x+16, self.rect.y+16, "spiky")
        enemy.add(enemyGroup) 
        self.spiky_spawnnumber += self.spiky_spawn_time
        self.busy_spawning_spiky = 0
