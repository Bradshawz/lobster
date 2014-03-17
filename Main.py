import pygame
from pygame.locals import *
from sys import exit

from Player import *
from Block import *
from Enemy import *
from Map import *
from Spawner import *

# Debug
DEBUG = True

# Init pygame & create a screen
pygame.init()
screen = pygame.display.set_mode((608,448),0,24)

# Create a clock to use to hold the framerate constant
clock = pygame.time.Clock()

# Initialize font for printing to screen
myfont = pygame.font.SysFont("monospace", 15)

# Create a white background
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill(pygame.Color(255,255,255))

# Set the window title and game font
pygame.display.set_caption("Horde")
game_font = pygame.font.SysFont("comicsansms",30)

# Create the map
game_map = Map("getonmy.lvl")
blockGroup = pygame.sprite.Group()
for block in game_map.get_blocks():
    block.add(blockGroup)
spawnerGroup = pygame.sprite.Group()
for spawner in game_map.get_spawner():
    spawner.add(spawnerGroup)


# Create the player
playerGroup = pygame.sprite.GroupSingle() # Create the Group
player = Player("lobster_standing.png", game_map.get_player_pos()) # Create the player Sprite
player.add(playerGroup) # Add the player Sprite to the Group

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
    
    # --------------------------------------------
    # Player Movement & Collisions
    # --------------------------------------------
    
    # Update player based on keyboard input
    keys_down = pygame.key.get_pressed() # Get a list of all keys pressed right now
    for p in playerGroup.sprites():
        p.update(keys_down, blockGroup.sprites())

    #--------------------------------------------
    # Enemy Movement    
    #--------------------------------------------
    for enemy in enemyGroup:
        enemy.update(blockGroup.sprites())

    #---------------------------------------------
    # Monster Spawning
    #---------------------------------------------
    for spawner in spawnerGroup:
        spawner.spawn(enemyGroup)
    # --------------------------------------------
    # Redraw everything on the screen
    # --------------------------------------------
    
    # Redraw the Background
    screen.blit(bg, (0,0))
    
    # Redraw all Groups
    blockGroup.draw(screen)
    enemyGroup.draw(screen)
    playerGroup.draw(screen)
    spawnerGroup.draw(screen)
    

    # Render text for debug
    if DEBUG:
        label = myfont.render("fps:"+str(int(clock.get_fps()))
                              +" monsters:"+str(len(enemyGroup)), 
                              1, (0,0,0))
        screen.blit(label, (20, 10))


    # Update the display
    pygame.display.update()
    
    # --------------------------------------------
    # Clock Tick
    # --------------------------------------------
    clock.tick(60)
