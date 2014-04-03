import pygame
import random
import Physics

class Enemy(pygame.sprite.Sprite):
    """
    Enemy character.
    
    Can move and kill the player.
    Has an image, rect-bounds.
    """
    BASE_MOVE_SPEED = 1

    def __init__(self, image_filename, pos_x, pos_y):
        """
        Pass in the filename of the image to represent
        this enemy.
        """
        # ------------------------------------------------
        # Call super constructor, set image and rect
        # ------------------------------------------------
        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect(center=(pos_x,pos_y))
        
        self.move = random.randint(0,1)
        self.vel_x = 0
        self.vel_y = 0
        
        self.on_ground = False
        self.move_speed = 1
        self.max_move_speed = 3
        
    """
    Block Collision
    """
    def collide(self, xvel, yvel, blocks):
        for block in [blocks[i] for i in self.rect.collidelistall(blocks)]:            
            # Check for collision on the sides
            if xvel > 0:
                # going -->
                if block.can_jump_through:
                    if self.rect.right - xvel < block.rect.left:
                        self.rect.right = block.rect.left
                else:
                    self.rect.right = block.rect.left
            if xvel < 0:
                # going <--
                if block.can_jump_through:
                    if self.rect.left - xvel > block.rect.right:
                        self.rect.left = block.rect.right
                else:
                    self.rect.left = block.rect.right
            
            # Check for falling collision
            if yvel > 0:
                if self.rect.bottom - yvel < block.rect.top:
                    self.rect.bottom = block.rect.top
                    self.on_ground = True
                    self.vel_y = 0
            
            # Check for jumping collision
            if yvel < 0:
                # Check for jump-through-able block
                if block.can_jump_through:
                    pass
                else:
                    if self.rect.top - yvel > block.rect.bottom:
                        self.rect.top = block.rect.bottom
                        self.vel_y = 0
    
    """
    Update enemy based on key input, gravity and collisions
    """
    def update(self, blocks, screen, waypoint, player):
        
        #Update movement
        self.basic_movement(waypoint, player)

        # Left/right movement
        if self.move == 0:
            # Go faster
            self.vel_x -= self.move_speed
            # But not too fast
            if self.vel_x < -1 * self.max_move_speed:
                self.vel_x = -1 * self.max_move_speed
        if self.move == 1:
            # Go faster
            self.vel_x += self.move_speed
            # But not too fast
            if self.vel_x > self.max_move_speed:
                self.vel_x = self.max_move_speed
        
        # Gravity
        if not self.on_ground:
            self.vel_y += Physics.gravity
            if self.vel_y > Physics.terminal_gravity:
                self.vel_y = Physics.terminal_gravity

        # Looping Across screen
        if self.rect.top >= screen.get_size()[1]+16:
            self.rect.bottom = 0
        if self.rect.bottom <= 0-8:
            self.rect.top = screen.get_size()[1]-8
            
        # If not moving left or right, stop.
        #  if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        #     self.vel_x = 0
            
        # Move horizontally, then handle horizontal collisions
        self.rect.left += self.vel_x
        self.collide(self.vel_x, 0, blocks)
        
        # Move vertically, then handle vertical collisions
        self.rect.top += self.vel_y
        self.on_ground = False
        self.collide(0, self.vel_y, blocks)
        

    def basic_movement(self, waypoint, player):
        """
        The basic movement for an enemy. If the player is on the 
        same platform region as the player, move toward the player.
        Otherwise move towards the nearest edge, using waypoints.
        """

        if abs(player.rect.bottom - self.rect.top) < 16:
            if player.rect.right > self.rect.right:
                return 1
            else:
                return 0

        for w in waypoint:
            if w:
                pass
            
            
