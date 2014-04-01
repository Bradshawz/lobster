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
    
    def __init__(self, images_dict, bottomleft):
        """
        Pass in the filename of the image to represent
        this player.
        
        images_dict should have:
            keys: 'standing', 'walking'
            values: a list of image filenames
        """        
        # Call the parent class (Sprite) constructor)
        pygame.sprite.Sprite.__init__(self)
        
        # Create images for all of the animations, and set the default image
        self.images = dict()
        for anim_type, image_filenames in images_dict.items():
            self.images[anim_type] = []
            for cur_image_filename in image_filenames:
                self.images[anim_type].append(pygame.image.load(cur_image_filename).convert_alpha())
        self.image = self.images['standing'][0]
        
        self.anim_image_walking = 0
        self.anim_image_jumping = 0
        self.anim_frame_counter_walking = 0
        self.anim_frame_counter_jumping = 0
        self.anim_frame_max_walking = 2
        self.anim_frame_max_jumping = 8
        
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
            if self.vel_y > Physics.terminal_gravity:
                self.vel_y = Physics.terminal_gravity
            
        # If not moving left or right, stop.
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.vel_x = 0
            
        # Move horizontally, then handle horizontal collisions
        self.rect.left += self.vel_x
        self.collide(self.vel_x, 0, blocks)
        
        # Move vertically, then handle vertical collisions
        self.rect.top += self.vel_y
        self.on_ground = False
        self.collide(0, self.vel_y, blocks)
        
        # TODO fix these anims
        
        # Standing Animation
        if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.image = self.images['standing'][0]
        # Jumping Animation
        elif not self.on_ground:
            # Animate the jumping!
            self.anim_frame_counter_jumping = (self.anim_frame_counter_jumping + 1) % self.anim_frame_max_jumping
            if self.anim_frame_counter_jumping == 0:
                self.anim_image_jumping = (self.anim_image_jumping + 1) % len(self.images['jumping'])
                self.image = self.images['jumping'][self.anim_image_jumping]
        # Walking Animation
        elif (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.on_ground:
            # Animate the walking!
            self.anim_frame_counter_walking = (self.anim_frame_counter_walking + 1) % self.anim_frame_max_walking
            if self.anim_frame_counter_walking == 0:
                self.anim_image_walking = (self.anim_image_walking + 1) % len(self.images['walking'])
                self.image = self.images['walking'][self.anim_image_walking]
        