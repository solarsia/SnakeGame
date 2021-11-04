import pygame
import time
import random

# Initialise Pygame
pygame.init()

# Display size
dis_width = 1000
dis_height = 700
# Snake
snake_block = 10
snake_speed = 27
# Timer
clock = pygame.time.Clock()
# Colours
background_colour = [30, 49, 55] # Dark Blue
snake_colour = (72, 136, 193) # Blue
text_colour = (71, 113, 158) # Medium Blue
food_colour = (172, 95, 217) # Magenta
# Font
font_style = pygame.font.SysFont("Helvetica", 40)

# Create Window
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")

# Message 
def message(msg,colour):
    mesg = font_style.render(msg,True,colour)
    display.blit(mesg, [200,320])

def draw_snake(snake_block,snake_list):
    # Drawing each square of the snake
    for position in snake_list:
        pygame.draw.rect(display,snake_colour,(position[0],position[1],snake_block, snake_block))

def score(score):
    # Render and display the message
    mesg = font_style.render("Your Score:" + str(score),True,text_colour)
    display.blit(mesg, [1,1])

def game_Loop():
    game_close = False
    game_over = False

    # Used to prevent the snake from going back on itself
    direction = ""

    # Snake Position
    x1 = dis_width/2
    y1 = dis_height/2
    # Update Snake Position
    x1_change = 0
    y1_change = 0

    # Draw food
    food_x = round(random.randrange(0,dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0,dis_height - snake_block) / snake_block) * snake_block

    # Length of snake
    length_snake = 1
    snake_list = []

    # Game Loop
    while not game_close:
        # Player looses, quit or play again
        while game_over == True:
            # Quit or play again
            display.fill(background_colour)
            message("You lost, press Q to quit or C to play again!", text_colour)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_Loop()


        # Play the game or press X to quit
        for event in pygame.event.get():
            # If User Quits Game Close Window
            if event.type == pygame.QUIT:
                game_close = True
            
            # Move the snake left, right, up and down
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (direction != "right" or direction == ""):
                    direction = "left"
                    x1_change = -snake_block
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT) and (direction != "left" or direction == ""):
                    direction = "right"
                    x1_change = snake_block
                    y1_change = 0
                elif (event.key == pygame.K_UP) and (direction != "up" or direction == ""):
                    direction = "down"
                    x1_change = 0
                    y1_change = -snake_block
                elif (event.key == pygame.K_DOWN) and (direction != "down" or direction == ""):
                    direction = "up"
                    x1_change = 0
                    y1_change = snake_block
        
        # Check boundaries
        if(x1 == 0 or x1 == dis_width or y1 == 0 or y1 == dis_height):
            game_over = True
        
        # Update Snake Position 
        x1 += x1_change
        y1 += y1_change

        # Colour Background
        display.fill(background_colour)
        
        # Draw Food
        pygame.draw.rect(display,food_colour,(food_x,food_y,snake_block, snake_block))

        # Draw Snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Delete the previous position of the snake if the length of the snake list is greater than the snake length
        if (len(snake_list) > length_snake):
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # Draw snake
        draw_snake(snake_block,snake_list)
        # State the score
        score(length_snake -1)
        pygame.display.update()

        # Update Food Position
        if (food_x == x1 and food_y == y1):
            food_x = round(random.randrange(0,dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0,dis_height - snake_block) / snake_block) * snake_block
            length_snake += 1

        # Snake speed
        clock.tick(snake_speed)

    # Quit Game
    pygame.quit()
    quit()

game_Loop()