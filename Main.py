import pygame
from pygame.locals import *
from sys import exit

from Player import *
from Enemy import *

# Init pygame & create a screen
pygame.init()
screen = pygame.display.set_mode((640,480),0,24)

# Create a white background
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill(pygame.Color(255,255,255))

# Set the window title and game font
pygame.display.set_caption("Horde")
game_font = pygame.font.SysFont("comicsansms",30)

# Create the player
playerGroup = pygame.sprite.GroupSingle() # Create the Group
player = Player("player_tmp.png") # Create the player Sprite
player.add(playerGroup) # Add the player Sprite to the Group

# Create an enemy group
enemyGroup = pygame.sprite.Group() # Create the Group

pygame.display.update()

# --------------------------------------------
# Main Game Loop
# --------------------------------------------
while True:
    # --------------------------------------------
    # Key Press Handling
    # --------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.event.pump()
    
    # --------------------------------------------
    # Key Press Handling
    # --------------------------------------------
    
    # If any keys are down
    if pygame.key.get_focused():
        # Get a list of all keys pressed right now
        key_down = pygame.key.get_pressed()
        
        if key_down[pygame.K_LEFT]:
            player.move_left()
        if key_down[pygame.K_RIGHT]:
            player.move_right()
        if key_down[pygame.K_UP]:
            player.move_up()
        if key_down[pygame.K_DOWN]:
            player.move_down()


    #--------------------------------------------
    # Enemy Movement    
    #--------------------------------------------
    for enemy in enemyGroup:
        enemy.move_random()

    #---------------------------------------------
    # Monster Spawning
    #---------------------------------------------
    if pygame.time.get_ticks() != 0:
        enemy = Enemy("enemy_tmp.png") # Create the enemy
        enemy.add(enemyGroup) # Add the enemy Sprite to the Group
    # --------------------------------------------
    # Redrawing
    # --------------------------------------------
    
    # Redraw the Background
    screen.blit(bg, (0,0))
    
    # Redraw all Groups
    playerGroup.draw(screen)
    # enemiesGroup.draw(screen) # to be added in later
    enemyGroup.draw(screen)
    # Update the display
    pygame.display.update()
