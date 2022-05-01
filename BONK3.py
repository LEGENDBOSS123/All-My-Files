class PLATFORM():
    def __init__(self, x, y, color, width, height, bounce, angle):
        self.location = (x,y, width, height)
        self.bounce = bounce
        self.color = color
        self.angle = angle
        
        self.image_o = pygame.Surface((self.location[2],self.location[3]))
        self.image_o.set_colorkey(bg)
        self.image_o.fill(self.color)

        self.rect = self.image_o.get_rect()
        self.rect.center = (self.location[0],self.location[1])

        self.new_im = pygame.transform.rotate(self.image_o,self.angle)
        self.rect = self.new_im.get_rect()
        self.rect.center = ((self.location[0],self.location[1]))
        
    def update(self):
        self.image_o = pygame.Surface((self.location[2],self.location[3]))
        self.image_o.set_colorkey(bg)
        self.image_o.fill(self.color)

        self.rect = self.image_o.get_rect()
        self.rect.center = (self.location[0],self.location[1])

        self.new_im = pygame.transform.rotate(self.image_o,self.angle)
        self.rect = self.new_im.get_rect()
        self.rect.center = ((self.location[0],self.location[1]))
        
    def draw(self):
        self.update()
        wn.blit(self.new_im,self.rect)
