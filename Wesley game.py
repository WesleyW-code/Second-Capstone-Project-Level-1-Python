# WESLEY'S GAME #

# ** Used the example as a template **

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1250
screen_height = 750
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy images and prize image).
# ** Images created by Kilmer & Cruise - https://kilmerandcruise.com/ **
# ** Prize image from Google images ** 

player = pygame.image.load("1.png")
enemy = pygame.image.load("3.png")
enmy_2 = pygame.image.load("5.png")# Adding enemy 2
enmy_3 = pygame.image.load("6.png")# Adding enemy 3
prize = pygame.image.load("prize.png") # Adding prize object

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enmy_2_height = enmy_2.get_height()
enmy_2_width = enmy_2.get_width()
enmy_3_height = enmy_3.get_height()
enmy_3_width = enmy_3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)# Start off screen at a random y position.
enmy_2XPosition = screen_width
enmy_2YPosition = random.randint(0, screen_height - enemy_height)# Start off screen at a random y position.
enmy_3XPosition = screen_width
enmy_3YPosition = random.randint(0, screen_height - enemy_height)# Start off screen at a random y position.

# Make the prize start off screen and at a random y position.

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)# Start off screen at a random y position.

# This checks if the up ,down ,left and right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keylft = False
keyrght = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))# This draws the enemy image to the screen.
    screen.blit(enmy_2, (enmy_2XPosition, enmy_2YPosition))# This draws the enemy image to the screen.
    screen.blit(enmy_3, (enmy_3XPosition, enmy_3YPosition))# This draws the enemy image to the screen.
    screen.blit(prize, (prizeXPosition, prizeYPosition)) # This draws the prize image to the screen
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN: # pygame.K_DOWN represents a keyboard key constant.
                keyDown = False


         # This event checks if the user press a key down.
         
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_LEFT: # pygame.K_LEFT represents a keyboard key constant.
                keylft = True
            if event.key == pygame.K_RIGHT:
                keyrght = True

        # This event checks if the key is up(i.e. not pressed by the user).

        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_LEFT:
                keylft = False
            if event.key == pygame.K_RIGHT: # pygame.K_RIGHT represents a keyboard key constant.
                keyrght = False

        
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keylft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player left of the window.
            playerXPosition -= 1
    if keyrght == True:
        if playerXPosition < screen_width - image_width:# This makes sure that the user does not move the player right of the window.
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We then need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enmy_2Box = pygame.Rect(enmy_2.get_rect())
    enmy_2Box.top = enmy_2YPosition
    enmy_2Box.left = enmy_2XPosition

    enmy_3Box = pygame.Rect(enmy_3.get_rect())
    enmy_3Box.top = enmy_3YPosition
    enmy_3Box.left = enmy_3XPosition

    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the enemy boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enmy_2Box) or playerBox.colliderect(enmy_3Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    # Test collision with the prize box:

    if playerBox.colliderect(prizeBox):

        # Display winning status to the user:

        print("You win!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
        
    # If the enemies are off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width and enmy_2XPosition < 0 - enmy_2_width and enmy_3XPosition < 0 - enmy_3_width :
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.45
    enmy_2XPosition -= 0.55
    enmy_3XPosition -= 0.50

    # Make the prize approach the player.
    
    prizeXPosition -= 0.48
    
    # ================The game loop logic ends here. =============
  
