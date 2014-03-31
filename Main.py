import pygame
from pygame.locals import *
from sys import exit

import Character, Player, Block

# Window Constants, Application Constants
# TODO refactor these into a Screen/Window/etc class
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 640

# Init pygame & create a screen
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,24)

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
platform_test = Block("platform_tile_blue.png", x=WINDOW_WIDTH/2, y=WINDOW_HEIGHT/2).add(blockGroup)

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
    
    # Player keyboard movement
    if pygame.key.get_focused():
        key_down = pygame.key.get_pressed() # Get a list of all keys pressed right now
        
        if key_down[pygame.K_LEFT]:
            player.accel_left()
        elif key_down[pygame.K_RIGHT]:
            player.accel_right()
        else:
            player.decel
        if key_down[pygame.K_UP]:
            player.accel_up()
        if key_down[pygame.K_DOWN]:
            player.accel_down()
            
    # Player Collision with Blocks
    collisions = pygame.sprite.groupcollide(playerGroup, blockGroup, False, False)
    for player_sprite, block_sprites in collisions.items():
        for block_sprite in block_sprites:
            # If their new rects collide, use their pixel mask to check if they really do collide
            if pygame.sprite.collide_mask(player_sprite, block_sprite):
                # COLLISION!
                player_sprite.handle_static_collision(block_sprite)
    
    # Actually move the player to where it should be
    player.move()
    
    # --------------------------------------------
    # Redrawing
    # --------------------------------------------
    
    # Redraw the Background
    screen.blit(bg, (0,0))
    
    # Redraw all Groups
    playerGroup.draw(screen)
    blockGroup.draw(screen)
    # enemiesGroup.draw(screen) # to be added in later
    
    # Update the display
    pygame.display.update()
    
    # --------------------------------------------
    # Clock Tick
    # --------------------------------------------
    clock.tick(120)
