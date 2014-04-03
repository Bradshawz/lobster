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
debugfont = pygame.font.SysFont("monospace", 15)

# Create a white background
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill(pygame.Color(255,255,255))

# Set the window title and game font
pygame.display.set_caption("Horde")
gamefont = pygame.font.SysFont("comicsansms",30)

# Create the map
game_map = Map("getonmy.lvl")

blockGroup = pygame.sprite.Group()
blockGroup.add([block for block in game_map.get_blocks()])

spawnerGroup = pygame.sprite.Group()
spawnerGroup.add([spawner for spawner in game_map.get_spawner()])

waypointList = game_map.get_waypoints()

# Create the player
playerGroup = pygame.sprite.GroupSingle() # Create the Group
player_anims = {"standing" : ["lobster_standing.png"],
                "walking"  : ["lobster_walking_0.png",
                              "lobster_walking_1.png"],
                "jumping"  : ["lobster_jumping_0.png",
                              "lobster_jumping_1.png"]
                }
player = Player(player_anims, game_map.get_player_pos()) # Create the player Sprite
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

    for p in playerGroup:
        p.update(keys_down, blockGroup, enemyGroup, screen)

    #--------------------------------------------
    # Enemy Movement    
    #--------------------------------------------
    
    for e in enemyGroup:
        e.update(blockGroup, screen, waypointList, player)

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
    spawnerGroup.draw(screen)
    enemyGroup.draw(screen)
    playerGroup.draw(screen)

    # Render text for debug
    if DEBUG:
        label = debugfont.render("fps:"+str(int(clock.get_fps()))
                              +" monsters:"+str(len(enemyGroup))
                              +" points: " + str(playerGroup.sprites()[0].points)
                              +" health: " + str(playerGroup.sprites()[0].health)
                              
                              , 1, (0,0,0))
        screen.blit(label, (20, 10))


    # Update the display
    pygame.display.update()
    
    # --------------------------------------------
    # Clock Tick
    # --------------------------------------------
    clock.tick(60)
