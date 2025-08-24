import pygame #imported pygame
pygame.init() #initialised it
import time #time module imported

#constant attributes for the screen size
X,Y = 600, 600

#creating the window for screen size
window = pygame.display.set_mode((X, Y))
caption = pygame.display.set_caption("Pong")
clock = pygame.time.Clock() #measuring the clock cycles of the CPU and FPS

#Creating Paddle Objects with relevant attributes with Object Oriented Programming
class paddle(object):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.velocity = 10
        self.colour = (255, 255, 255)
        self.score = 0

    #Methods for collisions, only accessible to the particular class (encapsulation)
    def hit(self, x, y):
        self.x = x
        self.y = y

#Creating Ball Objects with relevant attributes with Object Oriented Programming
class ball(object):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.x_velocity = 5
        self.y_velocity = 0
        self.colour = (255, 255, 255)
    
    #Method for moving the ball and collision only accessible to the particular class (encapsulation)
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
    
    def hit(self, x, y):
        self.x = x
        self.y = y

#Subroutine and Function for collision (Needed assistance for collision)
def collision(ball, paddle1, paddle2):
    if ball.y + ball.length >= Y:
        ball.y_velocity *= -1
    elif ball.y - ball.length <= 0:
        ball.y_velocity *= -1
    
    #Collision between paddle 1 and the ball
    if ball.x_velocity < 0:
        if ball.y >= paddle1.y and ball.y <= paddle1.y + paddle1.width:
            if ball.x <= paddle1.x + paddle1.length:
                ball.x_velocity *= -1  

                #Differentiation and Gradient identifying the direction of the ball after collision (Needed assistance for collision)
                middle_y = paddle1.y + paddle1.width / 2
                difference_y = middle_y - ball.y
                reduction_factor = (paddle1.width / 2) / ball.x_velocity
                y_velocity = difference_y / reduction_factor
                ball.y_velocity = y_velocity
    else:
        #Collision between paddle 2 and the ball
        if ball.y >= paddle2.y and ball.y <= paddle2.y + paddle2.width:
            if ball.x + ball.length >= paddle2.x:
                ball.x_velocity *= -1

                #Differentiation and Gradient identifying the direction of the ball after collision (Needed assistance for collision)
                middle_y = paddle2.y + paddle2.width / 2
                difference_y = middle_y - ball.y
                reduction_factor = (paddle2.width / 2) / ball.x_velocity
                y_velocity = difference_y / reduction_factor
                ball.y_velocity = y_velocity

#Function for drawing the line across half the distance with relevant attributes with Prodecural Programming Paradigm            
def draw():
    x = (X / 2)
    y = 0
    length = 5
    width = Y
    colour = (255, 255, 255)
    text = font.render(str(paddle1.score), 1, (255, 255, 255)) #Determines the score for paddle 1
    window.blit(text, ((X / 2) / 2, 0))
    text = font.render(str(paddle2.score), 1, (255, 255, 255)) #Determines the score for paddle 2
    window.blit(text, ((X + (X / 2)) / 2, 0))

    pygame.draw.rect(window, colour, (x, y, length, width)) #Drawing the line
    pygame.display.update() #Updates when any changes are made to the program and dispalyed on the screen

font = pygame.font.SysFont("Agency FB", 80, "Bold", True) #Dispalying the font
paddle1 = paddle(5, 250, 10, 100) #Creates Paddle 1 with relevant attributes
paddle2 = paddle(585, 250, 10, 100) #Creates Paddle 2 with relevant attributes
square_ball = ball(300, 300, 20, 20) #Creates ball with relevant attributes

run = True #Boolean variable to identify the operation of the window and code
#Iterating over the events taking place whilst executing
while run:
    clock.tick(60) #60 FPS

    for event in pygame.event.get(): #Checks for events in pygame and interactions from the user through Event Driven Programming Paradigms
        if event.type == pygame.QUIT: #Checks for the "X" (close) button on the top right hand corner
            run = False #Breaks out of the loop to close the game
    
    keys = pygame.key.get_pressed() #Used to identify any keys pressed by the user

#Used to move both paddles 1 and 2
    if keys[pygame.K_UP] and paddle2.y > paddle2.velocity:
        paddle2.y -= paddle2.velocity

    if keys[pygame.K_DOWN] and paddle2.y < Y - paddle2.velocity - paddle2.width:
        paddle2.y += paddle2.velocity

    if keys[pygame.K_w] and paddle1.y > paddle1.velocity:
        paddle1.y -= paddle1.velocity

    if keys[pygame.K_s] and paddle1.y < Y - paddle1.velocity - paddle1.width:
        paddle1.y += paddle1.velocity
    
    square_ball.move() #Procedure / Subroutine used to move the square ball around
    collision(square_ball, paddle1, paddle2) #Procedure / Subroutine used for detecting collisions between the paddles and the ball

    #Scoring System used depending on if the ball hits the end of the screen
    if square_ball.x == X - square_ball.length: #Checks if the screen hits the right hand side (side of paddle 2)
        paddle1.score += 1 #Increments score for paddle 1  
        time.sleep(0.5)

        #Rearranges the paddles and ball back to original position
        square_ball.hit(300, 300)
        paddle1.hit(5, 250)
        paddle2.hit(585, 250)

    if square_ball.x == 0: #Checks if the screen hits the left hand side (side of paddle 1)
        paddle2.score += 1 #Incements score for paddle 2  
        time.sleep(0.5)

        #Rearranges the paddles and ball back to original position
        square_ball.hit(300, 300)
        paddle1.hit(5, 250)
        paddle2.hit(585, 250)
    
    window.fill((0, 0, 0)) #Fills the screen
    pygame.draw.rect(window, paddle1.colour, (paddle1.x, paddle1.y, paddle1.length, paddle1.width)) #Creates and draws the paddle with the relevant attributes
    pygame.draw.rect(window, paddle2.colour, (paddle2.x, paddle2.y, paddle2.length, paddle2.width)) #Creates are draws the paddle with relevant attributes
    pygame.draw.rect(window, square_ball.colour, (square_ball.x, square_ball.y, square_ball.length, square_ball.width)) #Creates and draws the ball with relevant attributes
    line = draw() #Draws the line
    pygame.display.update() #Updates when any changes are made to the program and dispalyed on the screen
pygame.quit() #Quits the program