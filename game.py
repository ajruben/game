import pygame
import sys
pygame.init()

#stuff we need, display, images, clock
run = True
win = pygame.display.set_mode((700,600))
pygame.display.set_caption('Smeagol')
bg1 = pygame.image.load('mordor2.png')
bg2 = pygame.image.load('shire.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()

#We want to instantiate player
class Player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.walkCount = 0
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount=0
        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))
            
#for managing scenes, in each scene we want a certain gameloop
class GameState():
    def __init__(self):
        self.state = 'mordor_scene'
    
    def state_manager(self):
        if self.state == 'mordor_scene':
            self.mordor_scene()
        if self.state == 'hobbit_scene':
            self.scene_2()
    
    
    def mordor_scene(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_LEFT] and smeagol.x>smeagol.vel:
            smeagol.x -= smeagol.vel
            smeagol.left = True
            smeagol.right = False
        elif keys[pygame.K_RIGHT]:
            smeagol.x += smeagol.vel
            smeagol.right = True
            smeagol.left = False
        else:
           smeagol.right = False
           smeagol.left = False
           smeagol.walkCount = 0
        
        if not(smeagol.isJump):
            if keys[pygame.K_SPACE]:
                smeagol.isJump = True
                smeagol.right = False
                smeagol.left = False
                smeagol.walkCount =0
        else:
            if smeagol.jumpCount >= -10:
                neg=1
                if smeagol.jumpCount < 0:
                    neg =-1
                
                smeagol.y -= neg*(smeagol.jumpCount ** 2)/2
                smeagol.jumpCount -=1
            else:
               smeagol.isJump = False
               smeagol.jumpCount = 10
        redrawGameWindow(self.state)
        if smeagol.x > 700+smeagol.vel:
            smeagol.x = 0 - smeagol.vel
            self.state=='schire_scene'
    
    def shire_scene(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_LEFT] and smeagol.x>smeagol.vel:
            smeagol.x -= smeagol.vel
            smeagol.left = True
            smeagol.right = False
        elif keys[pygame.K_RIGHT] and smeagol.x<700-smeagol.width-smeagol.vel:
            smeagol.x += smeagol.vel
            smeagol.right = True
            smeagol.left = False
        else:
           smeagol.right = False
           smeagol.left = False
           smeagol.walkCount = 0
        
        if not(smeagol.isJump):
            if keys[pygame.K_SPACE]:
                smeagol.isJump = True
                smeagol.right = False
                smeagol.left = False
                smeagol.walkCount =0
        else:
            if smeagol.jumpCount >= -10:
                neg=1
                if smeagol.jumpCount < 0:
                    neg =-1
                
                smeagol.y -= neg*(smeagol.jumpCount ** 2)/2
                smeagol.jumpCount -=1
            else:
               smeagol.isJump = False
               smeagol.jumpCount = 10
    
        redrawGameWindow(self.state)

def redrawGameWindow(state):
    if state == 'mordor_scene':
        win.blit(bg1, (0,0))
        smeagol.draw(win)
    elif state == 'shire_scene':
        win.blit(bg2, (0,0))
        smeagol.draw(win)
    pygame.display.update()
    

#instances
smeagol = Player(0,500,64,64)
game_state = GameState()

while run:
    game_state.state_manager()
    clock.tick(27)
    
    
