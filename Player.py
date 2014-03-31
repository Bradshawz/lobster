import Character

class Player(Character):
    """
    Player character. Subclasses Character->Sprite.
    
    Can move, jump, attack.
    Has an image, health, rect-bounds.
    """
    BASE_HEALTH = 10
    
    def __init__(self, image_filename):
        super(Character, self).__init__(image_filename)
        
        self.on_ground = False
        self.health = self.BASE_HEALTH
        
    def jump(self):
        pass

    