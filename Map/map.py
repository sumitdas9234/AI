import pygame, sys, os, json

os.environ['SDL_VIDEO_CENTERED'] = '1'
background_colour = (178, 190, 195,1.0)
(width, height) = (1280, 650)
line = 0
global color
color =(247, 215, 148,0.7)
pygame.init()
global myfont
myfont = pygame.font.SysFont('Lucida Console', 12)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graph Coloring')
screen.fill(background_colour)

def colorGraph(screen):
    pallete = [(183, 21, 64,1.0),(243, 104, 224,1.0),(120, 111, 166,1.0),(231, 76, 60,1.0),(142, 68, 173,1.0)]
    available = [True,True, True, True, True]
    print(pallete[0])
    json_file1 = open('graph.json')
    json_file2 = open('map.json')
    graphs = json.load(json_file1)
    buildings = json.load(json_file2)
    graph = graphs['graph']
    building = buildings['buildings']
    for conn in graph:
        i=0
        color = pallete[i]
        for infra in building:
            if infra['name'] == conn['name']:
                render(screen, infra['location'], color)
                available[i] = False
                i+=1
                pygame.display.update()
                for neighbours in conn:
                    pass
    json_file1.close()
    json_file2.close()


def correct(key, screen):
    with open('map.json', 'r') as outfile:
        buildings = json.load(outfile)
        buildings = buildings['buildings']
        for building in buildings:
            for locations in building['location']:
                if locations == key:
                    print(building['name'])
                    push(screen,building['name'])
    outfile.close()

def init_console(screen,bgcolor):
    pygame.draw.rect(screen,bgcolor,(1015,0,1280-1015,650))
    pygame.display.update()
def push(screen, message):
    global line
    textsurface = myfont.render(message, True, (255, 255, 255))
    screen.blit(textsurface,(1020,line*10))
    line+=1
    pygame.display.update()
def showInfo(screen,pos):
    x = pos[0]
    y = pos[1]
    x = int(x / 25)
    y = int(y / 25)
    if correct([x,y], screen):
        pass
def render(screen, nodes, color):
    for node in nodes:
        pygame.draw.rect(screen,color,(node[0]*25,node[1]*25,25,25))
    pygame.display.update()

def init_ground(screen):
    for i in range(41):
        textsurface = myfont.render(str(i), True, (0, 0, 0))
        pygame.draw.line(screen,color,(i*25,0),(i*25,625),1)
        screen.blit(textsurface,(i*25,626))
    for i in range(26):
        textsurface = myfont.render(str(i), True, (0, 0, 0))
        pygame.draw.line(screen,color,(0,i*25),(1000,i*25),1)
        screen.blit(textsurface,(1001,i*25))

def init_map(screen):
    with open('map.json') as json_file:
        data = json.load(json_file)
        for building in data['buildings']:
            push(screen, "Rendering "+building["name"])
            render(screen,building['location'],building['color'])
        push(screen,"___________________________________________")
    json_file.close()
# init_ground(screen)
pygame.display.flip()

if __name__ == '__main__':

    init_console(screen,(44, 58, 71,1.0))
    init_map(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                mpos = pygame.mouse.get_pos()
                showInfo(screen, mpos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                colorGraph(screen)
