import pygame
import time
import random


pygame.init()

#colours 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 4, 5)
blue = (0, 0, 255)
yellow=(255,255,102)
green=(0,255,0)

#display window

displaywindow_width = 800
displaywindow_height = 600
 
displaywindow = pygame.display.set_mode((displaywindow_width, displaywindow_height))
pygame.display.set_caption('SnAke')
 
clock = pygame.time.Clock()

#snake dimension and speed 
snake_block = 10
snake_speed = 15
 
#font styles for score and ending sentences

font = pygame.font.SysFont("ariel", 30)
scorefont = pygame.font.SysFont("timesnewroman", 35)



#storing score
 
def Your_score(score):
    value = scorefont.render("Your Score: " + str(score), True, green)
    displaywindow.blit(value, [300, 200])


 
 
def gameLoop():  
    game_over = False
    game_close = False
 
    x1 = displaywindow_width / 2
    y1 = displaywindow_height / 2
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    snakelength = 1
 
    foodx = round(random.randrange(0, displaywindow_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, displaywindow_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            #game ending screen
            displaywindow.fill(red)
            
            mesg = font.render("You Lost! Press Q-Quit or C-Play Again", True, blue)
            displaywindow.blit(mesg, [displaywindow_width/4, displaywindow_height/2])
            Your_score(snakelength - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # movement in the display window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        #ending the game is snake goes out of the displayed window
        if x1 >= displaywindow_width or x1 < 0 or y1 >= displaywindow_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change

        
        displaywindow.fill(black)
        pygame.draw.rect(displaywindow, red, [foodx, foody, snake_block, snake_block],border_radius=5)

        
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snakelength:
            del snake_List[0]


        #ending game when snake bites itself 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        for x in snake_List:
            pygame.draw.rect(displaywindow, green, [x[0], x[1], snake_block, snake_block],)

        pygame.display.update()


        #generating food again once the snake eats it
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, displaywindow_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, displaywindow_height - snake_block) / 10.0) * 10.0
            snakelength += 1
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
