import pygame
from pygame.locals import *
from sys import exit

from Player import *
from Block import *
from Enemy import *
from Map import *
from Spawner import *

# Importing Timer to schedule things
# Example use:
# secondsToWait = 1.5
# list_of = player_sprite
# parameters = "new-image.jpg"
# def changeImage(player, filename) {
#     player.image = filename
# }
# changeImageTimer = Timer(secondsToWait, changeImage, [list_of, parameters])
# a la http://stackoverflow.com/questions/16578652/threading-timer
from threading import Timer

# Debug
DEBUG = True

# Init pygame & create a screen
pygame.init()
screen = pygame.display.set_mode((608,448),0,24)

# Create a clock to use to hold the framerate constant
clock = pygame.time.Clock()

# Initialize fonts for printing to screen
debugfont = pygame.font.SysFont("monospace", 15)
gamefont = pygame.font.SysFont("monospace",30)
game_label = gamefont.render("TestLabel", 1, (0,0,0))

# Create a white background
bg = pygame.Surface(screen.get_size())
bg = bg.convert()
bg.fill(pygame.Color(255,255,255))

# Set the window title and game font
pygame.display.set_caption("Horde")

# Create the map
game_map = Map("getonmy.lvl")

blockGroup = pygame.sprite.Group()
blockGroup.add([block for block in game_map.get_blocks()])

spawnerGroup = pygame.sprite.Group()
spawnerGroup.add([spawner for spawner in game_map.get_spawner()])

waypointList = game_map.get_waypoints()

# Create the player
playerGroup = pygame.sprite.GroupSingle() # Create the Group
player_anims = {"standing" : {"filenames" : ["images/lobster_standing.png"],
                              "frames_between" : 100,
                              },
                "walking"  : {"filenames" : ["images/lobster_walking_0.png",
                                             "images/lobster_walking_1.png"],
                              "frames_between" : 10
                              },
                "jumping"  : {"filenames" : ["images/lobster_jumping_0.png",
                                             "images/lobster_jumping_1.png"],
                              "frames_between" : 15
                              }
                }
player = Player(player_anims, game_map.get_player_pos()) # Create the player Sprite
player.add(playerGroup) # Add the player Sprite to the Group

# Create an enemy group
enemyGroup = pygame.sprite.Group() # Create the Group

# To be used on game restart or on
# player death/game over
def resetGame():
    global game_label # using the GLOBAL game_label
    game_label = gamefont.render("", 1, (0,0,0))
    player.reset()
    enemyGroup.empty()


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
    # Player: Movement, Collisions and Death
    # --------------------------------------------
    
    # Update player based on keyboard input
    keys_down = pygame.key.get_pressed() # Get a list of all keys pressed right now

    player.update(keys_down, blockGroup, enemyGroup, screen)
    if player.health <= 0:
        # Player has died
        if not player.currently_dying:
            player.currently_dying = True
            resetGameTimer = Timer(3.0, resetGame)
            resetGameTimer.start()
            game_label = gamefont.render("Game over! Points: {}".format(player.points),
                                         1, (0,0,0))
        

    #--------------------------------------------
    # Enemy Movement    
    #--------------------------------------------
    hasSquishedSomeoneAlready = False
    to_remove = None
    for e in enemyGroup:
        squished = e.update(blockGroup, screen, waypointList, player, hasSquishedSomeoneAlready)
        if squished:
            to_remove = e
            hasSquishedSomeoneAlready = True
    if to_remove != None:
        enemyGroup.remove(to_remove)
    
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
    
    # Draw game text
    width, height = screen.get_size()
    screen.blit(game_label, (width/4, height/2))

    # Render text for debug
    if DEBUG:
        label = debugfont.render("fps:"+str(int(clock.get_fps()))
                              +" monsters:"+str(len(enemyGroup))
                              +" points: " + str(player.points)
                              +" health: " + str(player.health)
                              
                              , 1, (0,0,0))
        screen.blit(label, (20, 10))


    # Update the display
    pygame.display.update()
    
    # --------------------------------------------
    # Clock Tick
    # --------------------------------------------
    clock.tick(60)
