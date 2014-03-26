import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Horde")
game_font = pygame.font.SysFont("comicsansms",30)
text = game_font.render("Horde", True, (0,0,0), (255,255,255))
image = pygame.image.load("player-tmp.png").convert_alpha()

screen.blit(image,(0,0))
screen.blit(text,(200,200))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


