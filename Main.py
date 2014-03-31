import pygame
from pygame.locals import *
from sys import exit

from Player import *
from Block import *
from Enemy import *

# Window Constants, Application Constants
# TODO refactor these into a Screen/Window/etc class
window_size = (640, 480)

# Init pygame & create a screen
pygame.init()
screen = pygame.display.set_mode(window_size,0,24)

# Create a clock to use to hold the framerate constant
clock = pygame.time.Clock()

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

# Create the map
# TODO refactor this into a Map or Level class maybe, i.e. Level.load, for block in Level.blocks, etc
blockGroup = pygame.sprite.Group()
platform_test = Block("block_blue.png", x=0, y=window_size[1]/2).add(blockGroup)
platform_test2 = Block("block_blue_10.png", x=16, y=window_size[1]/2 - 16).add(blockGroup)

# Create an enemy group
enemyGroup = pygame.sprite.Group() # Create the Group

# --------------------------------------------
# Main Game Loop
# --------------------------------------------
while True:
    # --------------------------------------------
    # Event Handling
    # --------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.event.pump()
    
    # --------------------------------------------
    # Movement & Collisions
    # --------------------------------------------
    
    # Update player based on keyboard input
    keys_down = pygame.key.get_pressed() # Get a list of all keys pressed right now
    for p in playerGroup:
        p.update(keys_down, blockGroup.sprites())

    #--------------------------------------------
    # Enemy Movement    
    #--------------------------------------------
    for enemy in enemyGroup:
        enemy.move_random()

    #---------------------------------------------
    # Monster Spawning
    #---------------------------------------------
#     if pygame.time.get_ticks() != 0:
#         enemy = Enemy("enemy_tmp.png") # Create the enemy
#         enemy.add(enemyGroup) # Add the enemy Sprite to the Group
    
    # --------------------------------------------
    # Redrawing
    # --------------------------------------------
    
    # Redraw the Background
    screen.blit(bg, (0,0))
    
    # Redraw all Groups
    playerGroup.draw(screen)
    blockGroup.draw(screen)
    enemyGroup.draw(screen)
    
    # Update the display
    pygame.display.update()
    
    # --------------------------------------------
    # Clock Tick
    # --------------------------------------------
    clock.tick(120)
