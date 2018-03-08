import pygame, sys, os, json, random
import pygame.time
os.environ['SDL_VIDEO_CENTERED'] = '1'
background_colour = (255, 255, 255)
(width, height) = (1000, 600)
line = 3
global color
color =(247, 215, 148,0.7)
pygame.init()
global myfont,targetfont
myfont = pygame.font.Font("raleway.ttf", 48)
targetfont = pygame.font.Font("raleway-bold.ttf", 24)
headingSmallfont = pygame.font.Font("raleway-bold.ttf", 24)
consolefont = pygame.font.Font("raleway.ttf", 20)
global screen,POPULATION_SIZE,consoleline
consoleline = 20
# Target string to be generated
TARGET = "What you see is what you get?"


# Number of individuals in each generation
POPULATION_SIZE = 1000

# Valid genes
GENES = '''abcdefghijklmnopqrstuv, .-;:_!"'wxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890#%&/()=?@${[]}'''



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('')
screen.fill(background_colour)
pygame.display.flip()

class Individual(object):
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        global GENES
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''

        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.40:
                child_chromosome.append(gp1)

            # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.80:
                child_chromosome.append(gp2)

            # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

        # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fittness score, it is the number of
        characters in string which differ from target
        string.
        '''
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness+= 1
        return fitness

def fitnessAnimate(fitness):
    end = 500  - (fitness/100)*400
    pygame.draw.line(screen,(50, 255, 126), [550, 500], [550,end], 3)
    pygame.display.update()


def heading(message,x,y):
    global line
    textsurface = myfont.render(message, True, (0, 0, 0))
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
    found = False
    heading("Generation:",50,15)
    heading("Current String:",50,70)
    heading("Fitness:",50,125)
    headingSmall("Steps Involved:",570,8*8)
    console("1. Create a New Generation.")
    console("2. Calculate the finess of each Individual.")
    console("3. Select 10% of the Population.")
    console("4. Mate or Mutate accordingly.")
    console("5. Repeat till '"+TARGET+"'")
    i = 0
    pygame.draw.line(screen,(255, 82, 82), [550, 100], [550,500], 2)
    #current generation
    generation = 1
    running = True
    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
                gnome = Individual.create_gnome()
                population.append(Individual(gnome))


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        while not found:
            pygame.time.delay(300)
            # sort the population in increasing order of fitness score
            population = sorted(population, key = lambda x:x.fitness)

            # if the individual having lowest fitness score ie.
            # 0 then we know that we have reached to the target
            # and break the loop
            if population[0].fitness <= 0:
                found = True

            # Otherwise generate new offsprings for new generation
            new_generation = []
            # Perform Elitism, that mean 10% of fittest population
            # goes to the next generation
            s = int((10*POPULATION_SIZE)/100)
            new_generation.extend(population[:s])
            # From 50% of fittest population, Individuals
            # will mate to produce offspring
            s = int((90*POPULATION_SIZE)/100)
            for _ in range(s):
                parent1 = random.choice(population[:50])
                parent2 = random.choice(population[:50])
                child = parent1.mate(parent2)
                new_generation.append(child)

            population = new_generation
            # print("Generation: {}\tString: {}\tFitness: {}".\
            #       format(generation,
            #       "".join(population[0].chromosome),
            #       population[0].fitness))
            generationShow(str(generation))
            currentfitness = (100 - int(population[0].fitness/len(TARGET)*100))
            target("".join(population[0].chromosome))
            fitnessShow("" + str(currentfitness)+" %")
            fitnessAnimate(currentfitness)
            generation += 1
