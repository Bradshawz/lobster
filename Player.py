import pygame
import Physics

class Player(pygame.sprite.Sprite):
    """
    Player character. Subclasses Character->Sprite.
    
    Can move, jump, attack.
    Has an image, health, rect-bounds. 
        
    Has:
    image, rect, mask
    
    Can:
    move itself
    
    Movement is done by "try"ing to move. This does not update the actual
    positions: just the "new" positions. The "move" method must be called every
    frame to update the actual position to the "new" calculated position.
    """
    
    def __init__(self, image_filename, bottomleft):
        """
        Pass in the filename of the image to represent
        this player.
        """        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image of the player Sprite
        self.image = pygame.image.load(image_filename).convert_alpha()
        # Set the collision mask based on the image
        self.mask = pygame.mask.from_surface(self.image)
        
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = bottomleft
        
        self.vel_x = 0
        self.vel_y = 0
        
        self.on_ground = False
        self.jump_speed = 7
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
                if self.rect.right - xvel < block.rect.left:
                    self.rect.right = block.rect.left
            if xvel < 0:
                # going <--
                if self.rect.left - xvel > block.rect.right:
                    self.rect.left = block.rect.right
            
            # Check for falling collision
            if yvel > 0:
                if self.rect.bottom - yvel < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.on_ground = True
                    self.vel_y = 0
            
            # Check for jumping collision
            if yvel < 0:
                # Check for jump-through-able block
                if block.can_jump_through:
                    pass
                else:
                    self.rect.top = block.rect.bottom
                    self.vel_y = 0
    
    """
    Update player based on key input, gravity and collisions
    """
    def update(self, keys, blocks):
        # Jumping
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y -= self.jump_speed
            self.on_ground = False
        
        # Left/right movement
        if keys[pygame.K_LEFT]:
            # Go faster
            self.vel_x -= self.move_speed
            # But not too fast
            if self.vel_x < -1 * self.max_move_speed:
                self.vel_x = -1 * self.max_move_speed
        if keys[pygame.K_RIGHT]:
            # Go faster
            self.vel_x += self.move_speed
            # But not too fast
            if self.vel_x > self.max_move_speed:
                self.vel_x = self.max_move_speed
        
        # Gravity
        if not self.on_ground:
            self.vel_y += Physics.gravity
            if self.vel_y > Physics.terminal_gravity: self.vel_y = Physics.terminal_gravity
            
        # If not moving left or right, stop.
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.vel_x = 0
            
        # Move horizontally, then check for horizontal collisions
        self.rect.left += self.vel_x
        self.collide(self.vel_x, 0, blocks)
        
        # Move vertically, then check for vertical collisions
        self.rect.top += self.vel_y
        self.on_ground = False
        self.collide(0, self.vel_y, blocks)
            