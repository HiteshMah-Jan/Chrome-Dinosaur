
import pygame
import sys

pygame.init()
pygame.font.init()
comic = pygame.font.SysFont('Comic Sans MS' , 30)

g =1
ground = 600
bg_color =  (250,0,250)
bg = pygame.image.load("D:\\0f43dec7616ff130b16986a254659069 (2).jpg")
(width,height) = (800, 800)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Dinosaur')
#img = pygame.image.load('D:\iitgoa_logo_wx.png')


class Dino():
    def __init__(self):
        self.image = pygame.image.load("D:\dinosaur.png")
        self.x = 200
        self.y = ground
        self.v = 0


    def jump(self):
        self.v = -30
        self.y -= 1


    def update(self):
        global g
        if self.y < ground:
            self.y = self.y + self.v
            self.v = self.v + g
        if self.y > ground:
            self.y = ground
            #print(self.y)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def hit(self, Cactus):
        dino_mask = self.get_mask()
        cac_mask = Cactus.get_mask()
        offset = (self.x-Cactus.x-25, self.y-ground)
        if dino_mask.overlap(cac_mask,offset):
            return True

        #if (abs(Cactus.x - self.x) < 145) and (self.y == ground):
        #    return True
        return False



class Cactus():
    def __init__(self):
        self.image = pygame.image.load("D:\cactus.png")
        self.x = 800


    def update(self):
        if self.x > -191:
            self.x -= 7
        else:
            self.x = 800

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def passed(self, Dino):
        return (Dino.x-5 < self.x < Dino.x+5)

run = True
d = Dino()
c = Cactus()

scr = 0
score = comic.render('Score = '+ str(scr), False, (250,250,250))
screen.blit(score,(0,0))

while run:
    screen.fill(bg_color)
    #screen.blit(bg,(c.x,0))
    #screen.blit(bg,(c.x-800,0))
    screen.blit(c.image,(c.x,ground))
    screen.blit(d.image,(d.x,d.y))
    screen.blit(score, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and d.y == ground:
        d.jump()
    if keys[pygame.K_y]:
        scr = 0
        d = Dino()
        c = Cactus()
    if keys[pygame.K_n]:
        sys.exit()

    if d.hit(c):
        scr = 0
        textsurface = comic.render(' OOPS!  Retry? -> Press  Y or N', False, (0,0,0))
        screen.blit(textsurface,(50,50))
    else:
        d.update()
        c.update()

    if c.passed(d):
        scr+=1
        score = comic.render('Score = ' + str(scr), False, (250, 250, 250))



    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()
