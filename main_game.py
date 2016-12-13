import pygame
import time
import random

#for background colors
green = (154, 205, 50)
orange = (255, 165, 0)
blue = (135, 206, 240)
black = (0,0,0)
white = (255,255,255)

#initiate pygame module
pygame.init()

#game title
pygame.display.set_caption('Flappy Bird Clone')


'''
if we load image file in bird function, then whenever that function is
called, it'll load the image everytime from the memory. But we want to
load the image just once.
'''
#bg = pygame.image.load('bg.png') #background image
img = pygame.image.load('bird1.png') #bird image
imgwd = 75
imght = 55

#set the resolution of the display frame
surfacewd = 1240
surfaceht = 650
surface = pygame.display.set_mode((surfacewd, surfaceht))

#set up frame per seconds (fps). The rate at which the frames will move
clock = pygame.time.Clock()

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: '+str(count), True, black)
    surface.blit(text, [0,0])

def blocks(x_block, y_block, blockwd, blockht, gap):
    pygame.draw.rect(surface, green, [x_block, y_block, blockwd, blockht])
    pygame.draw.rect(surface, green, [x_block, y_block+blockht+gap, blockwd, surfaceht])

def gameOver():
    msgSurface('Ooops you crashed!')
    pygame.quit()
    quit()

def bird(x, y, image):
    surface.blit(img, (x, y))

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    '''
    This function helps in printing messages on the screen in 2 sized, small and large
    '''
    smalltxt = pygame.font.Font('freesansbold.ttf', 20)
    largetxt = pygame.font.Font('freesansbold.ttf', 100)

    titleTextSurf, titleTextRect = makeTextObjs(text, largetxt)
    titleTextRect.center = surfacewd/2, surfaceht/2 #location of rectangle
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press Up arrow key to continue', smalltxt)
    typTextRect.center = surfacewd/2, ((surfaceht/2) + 100)
    surface.blit(typTextSurf, typTextRect)
    '''
    this prints large text. titleTextRect.center gives location of the rectangle in which
    text will be printed
    titleTextSurf, titleTextRect = makeTextObjs(text, largetxt) this is for printing a message
    same of followed for small text
    '''

    pygame.display.update() #this updates the surface
    time.sleep(1) #displays the message for atleast this time if inccase a key has been pressed

    while replay_or_quit == None:
        clock.tick()

    main() #to do anything besides quitting game, return to main loop

def main():
    x = 350
    y = 270
    bird_move = 0
    
    #xbg = 0
    #ybg = 0
    
    x_block = surfacewd
    y_block = 0
    
    blockwd = 75
    blockht = random.randint(0, surfaceht/2)
    gap = imght*3
    block_move = 4

    current_score = 0
    
    #to keep the game running till its not over
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            '''
            pygame constantly tracks all the events on the screen and
            returns the value. Like where the mouse is, what keys are
            being pressed and so on
            '''

            if event.type == pygame.QUIT:
                '''
                if the event type returned os for quitting the game then change
                variable game_over to True to end the game. Quit event triggers
                when we press X 
                '''

                game_over = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_move = -5
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bird_move = 5
            '''
            The above 2 if conditions check for user input. So KEYDOWN means that
            when a key is pressed on the keyboard, and the inner if condition
            checks that if that pressed key is "Key Up = K_UP", then move the
            bird up by 5. In Python Y increases as you go down. So to go up,
            you give negative value.

            The second if condition is when no key is pressed, in the event, when
            Key Up is not pressed, move the bird down
            '''

        y += bird_move
        
        #surface.blit(bg, (xbg, ybg))
        surface.fill(blue)
        bird(x, y, img)
        
        blocks(x_block, y_block, blockwd, blockht, gap)
        score(current_score)
        x_block -= block_move

        if y > (surfaceht-70) or y < (surfaceht-655):
            gameOver()

        if x_block < (-1*blockwd):
            x_block = surfacewd
            blockht = random.randint(0, surfaceht/2)
            current_score += 1

        if x+imgwd > x_block:
            if x < x_block + blockwd:
                if y < blockht-5:
                    if x - imgwd < blockwd + x_block:
                        gameOver()

        if x+imgwd > x_block:
            if y+imght+20 > blockht+gap:
                if x - 15 < blockwd + x_block:
                    gameOver()

        #if x_block < (x - blockwd) < x_block + block_move:
            #current_score += 1

        if 3 <= current_score < 5:
            block_move = 6
            gap = imght*2.75
        if 8 <= current_score < 10:
            block_move = 8
            gap = imght*2.5
        if 13 <= current_score < 15:
            block_move = 10
            gap = imght*2.25
        if 18 <= current_score < 20:
            block_move = 12
            gap = imght*2

        pygame.display.update()
        clock.tick(60) #60 fps
        '''
        display.update just updates specific areas on the screen. Whereas,
        display.flip() updates the entires window. If no parameters are passed
        to update, thenit will update the entire screen. Over here we are using
        it to update the clock
        '''
        
main()
pygame.quit()
quit()
