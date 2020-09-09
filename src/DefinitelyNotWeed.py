import pygame

NOT_A_WEED_IMAGE = pygame.image.load(os.path.join("assets", "definitely_not_weed.png"))

class DefinitelyNotWeed():


      def __init__(self):
        
        super().__init__()

        self.image = NOT_A_WEED_IMAGE
        self.rect = self.image.get_rect() 

    def update(self):
        

