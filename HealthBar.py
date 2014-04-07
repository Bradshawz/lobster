import pygame.sprite
from pygame import Rect

class HealthBar(pygame.sprite.Sprite):
    """
    A health bar.
    
    Is a rect filled with red.
    Has:
    - maximum health
    - current health
    - width
    - height
    Can:
    - decrease health
    - query health
    """


    def __init__(self, max_health, rect):
        """
        Takes:
        max_health (int),
        rect (Rect with x,y,width,height)
        """
        # Set defaults
        self.max_health = max_health
        self.current_health = max_health
        self.rect = rect
        
        self.image = pygame.Surface([self.rect.width, self.rect.height])
        self.image.fill((0,0,0))
        self.image.fill((255, 0, 0), self.get_fill_rect())
    
    def decrease(self):
        self.current_health -= 1
        # Reset the fill
        self.image.fill((0,0,0))
        self.image.fill((255, 0, 0), self.get_fill_rect())
    
    def set_current_health(self, current_health):
        self.current_health = current_health
    
    def get_health(self):
        return self.current_health
    
    def get_percentage_health(self):
        return self.current_health / self.maximum_health
    
    def get_fill_rect(self):
        fill_rect = self.rect
        fill_rect.topleft = (0,0) # Topleft of the image
        fill_rect.width *= self.get_percentage_health() # Scale the width
        return fill_rect