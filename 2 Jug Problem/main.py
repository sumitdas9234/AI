import pygame, sys, os, json, random
import pygame.time
os.environ['SDL_VIDEO_CENTERED'] = '1'
background_colour = (255, 255, 255)
(width, height) = (960, 640)
line = 3
global color
color =(247, 215, 148,0.7)
pygame.init()
global myfont,targetfont
myfont = pygame.font.Font("raleway.ttf", 32)
bracket = pygame.font.Font("raleway.ttf", 68)
targetfont = pygame.font.Font("raleway.ttf", 28)
headingSmallfont = pygame.font.Font("raleway-bold.ttf", 16)
consolefont = pygame.font.Font("raleway.ttf", 20)
global screen,POPULATION_SIZE,consoleline, image
consoleline = 20
image = pygame.image.load(os.path.join('res', 'jug.png'))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('')
screen.fill(background_colour)
pygame.display.flip()
global jugImage
global TARGET
TARGET = 1

class Jug(object):
    """docstring for Jug."""
    def __init__(self, capacity,x,y,anti=False):
        super(Jug, self).__init__()
        self.capacity = capacity
        self.currentVolume = 0
        self.anti = anti
        if anti:
            self.image = pygame.image.load(os.path.join('res', 'anti.png'))
            self.image = pygame.transform.scale(self.image, (44*self.capacity, 50*self.capacity))
        else:
            self.image = image
            self.image = pygame.transform.scale(self.image, (44*4, 50*4))
        screen.blit(self.image,(x,y))
        pygame.display.update()

    def showVolume(self):
        if self.anti:
            pygame.draw.rect(screen,(255,255,255),(410,line*132,70,70))
            brac(str(self.currentVolume),440,128)
        else:
            pygame.draw.rect(screen,(255,255,255),(270,line*132,70,70))
            brac(str(self.currentVolume),300,128)

    def updateVolume(self):
        if self.anti:
            currentfill = int((self.currentVolume/self.capacity)*110)
            pygame.draw.rect(screen,(255,255,255),(422,270,73,117))
            if currentfill != 0:
                pygame.draw.rect(screen,(24, 220, 255),(422,387 - currentfill,73,currentfill))
        else:
            currentfill = int((self.currentVolume/self.capacity)*147)
            pygame.draw.rect(screen,(255,255,255),(270,240,98,147))
            if currentfill != 0:
                pygame.draw.rect(screen,(24, 220, 255),(270,387 - currentfill,98,currentfill))
        self.showVolume()
        pygame.display.update()

    def isempty(self):
        if self.currentVolume == 0:
            return True
        else:
            return False

    def isfull(self):
        if self.currentVolume == self.capacity:
            return True
        return False

    def fill(self):
        if self.isfull():
            return False
        self.currentVolume = self.capacity
        # pygame.draw.rect(screen,(24, 220, 255),(237,250,73,137))
        self.updateVolume()
        return True

    def empty(self):
        if self.isempty():
            return False
        self.currentVolume = 0
        self.updateVolume()
        return True

    def transfer(self,destination):
        if self.isempty():
            return False
        if destination.isfull():
            return False
        if self.currentVolume <= (destination.capacity - destination.currentVolume):
            destination.currentVolume += self.currentVolume
            self.empty()
            self.updateVolume()
            destination.updateVolume()
            return True
        self.currentVolume -= (destination.capacity - destination.currentVolume)
        destination.currentVolume = (destination.capacity - destination.currentVolume)
        self.updateVolume()
        destination.updateVolume()
        return True



def fitnessAnimate(fitness):
    end = 500  - (fitness/100)*400
    pygame.draw.line(screen,(50, 255, 126), [550, 500], [550,end], 3)
    pygame.display.update()


def heading(message,x,y):
    global line
    textsurface = myfont.render(message, True, (0, 0, 0))
    screen.blit(textsurface,(x,line*y))
    pygame.display.update()


def info(message,x,y):
    global line
    textsurface = targetfont.render(message, True,(0, 0, 0))
    screen.blit(textsurface,(x,line*y))
    pygame.display.update()

def brac(message,x,y):
    global line
    textsurface = bracket.render(message, True,(0, 0, 0))
    screen.blit(textsurface,(x,line*y))
    pygame.display.update()

def headingSmall(message,x,y):
    textsurface = headingSmallfont.render(message, True, (0, 0, 0))
    screen.blit(textsurface,(x,line*y))
    pygame.display.update()

def target(message):
    global line
    textsurface = targetfont.render(message, True, (0, 0, 0))
    pygame.draw.rect(screen,(255,255,255),(50,line*13*7,len(TARGET)*17,100))
    screen.blit(textsurface,(50,line*13*7))
    pygame.display.update()

def console(message):
    global consoleline
    textsurface = consolefont.render(message, True, (0, 0, 0))
    screen.blit(textsurface,(560,consoleline*12))
    pygame.display.update()
    consoleline += 4

def generationShow(message):
    global line
    textsurface = myfont.render(message, True, (0, 0, 0))
    pygame.draw.rect(screen,(255,255,255),(120,110,300,100))
    screen.blit(textsurface,(120,110))
    pygame.display.update()

def fitnessShow(message):
    global line
    textsurface = myfont.render(message, True, (0, 0, 0))
    pygame.draw.rect(screen,(255,255,255),(100,430,300,100))
    screen.blit(textsurface,(100,430))
    pygame.display.update()

if __name__ == '__main__':
    A = Jug(5,220,205)
    B = Jug(3,400,251,True)
    found = False
    heading("Generation",100,5)
    pygame.draw.aaline(screen,(0, 0, 0), [325, 20], [325,150], 2)
    heading("Population",400,5)
    pygame.draw.aaline(screen,(0, 0, 0), [625, 20], [625,150], 2)
    heading("Fitness",700,5)
    heading("Current Action",625,65)
    heading("Fittest DNA",380,160)
    info("Volume",100,137)
    brac("=",200,128)
    brac("{               }",230,130)
    brac("  "+str(A.currentVolume)+"  ,  "+str(B.currentVolume), 253,128)
    pygame.draw.aaline(screen,(0, 0, 0), [20, 470], [940,470], 2)
    # pygame.draw.aaline(screen,(0, 0, 0), [250, 500], [250,387], 2)
    pygame.draw.aaline(screen,(0, 0, 0), [250, 387], [550,387], 2)
    pygame.draw.aaline(screen,(0, 0, 0), [550, 200], [550,470], 2)
    # console("5. Repeat till '"+TARGET+"' is found.")
    i = 0
    running = True
    pygame.display.flip()


    A.fill();
    pygame.time.delay(1000)
    B.fill();
    pygame.time.delay(1000)
    B.empty();
    pygame.time.delay(1000)
    A.transfer(B);
    pygame.time.delay(1000)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
