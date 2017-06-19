 
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
BROWN    = ( 122,  92,  48)
GREY     = ( 115, 115, 115)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")


 
# Loop until the user clicks the close button.
done = False

def House (screen, x, y):
    pygame.draw.rect(screen, WHITE, [500+x, 250+y, 250, 300])
    pygame.draw.rect(screen, BROWN, [500+x, 250+y, 250, 300], 4)
    pygame.draw.polygon(screen, BROWN, [[625+x, 100+y], [775+x, 250+y], [475+x, 250+y]],)
    pygame.draw.rect(screen, BROWN, [600+x, 470+y, 50, 80])
    pygame.draw.rect(screen, BLACK, [640+x, 510+y, 10, 5])
    pygame.draw.rect(screen, BLUE, [525+x, 300+y, 60, 70])
    pygame.draw.rect(screen, BLACK, [525+x, 300+y, 60, 70], 2)
    pygame.draw.rect(screen, BLACK, [525+x, 335+y, 60, 2])
    pygame.draw.rect(screen, BLACK, [554+x, 300+y, 2, 70])
    pygame.draw.rect(screen, BLUE, [665+x, 300+y, 60, 70])
    pygame.draw.rect(screen, BLACK, [665+x, 300+y, 60, 70], 2)
    pygame.draw.rect(screen, BLACK, [665+x, 335+y, 60, 2])
    pygame.draw.rect(screen, BLACK, [694+x, 300+y, 2, 70])
    
def tree (screen, v, b):
    pygame.draw.rect(screen, BROWN, [v, b, 50, 200])
    pygame.draw.ellipse(screen, GREEN, [-25+v, -100+b, 100, 200],50)
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x = 0
y = 0
v = 0
b = 0
# -------- Main Program Loop -----------
pygame.key.set_repeat(1,1)
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
            if event.key == pygame.K_LEFT:
                if(x <= -450):
                    break
                else:
                    x += -30
            elif event.key == pygame.K_RIGHT:
                if(x >= 470):
                    break
                else:
                    x += 30
            elif event.key == pygame.K_UP:
                if(y <= -90):
                    break
                else:
                    y += -30
            elif event.key == pygame.K_DOWN:
                if(y >= 150):
                    break
                else:
                    y += 30
        
               
                   
            # User let up on a key
        elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0        
        
    
 
    screen.fill(BLACK)
    House(screen,x, y)
    



    tree(screen, v, b)
    pos = pygame.mouse.get_pos()
    v = pos[0]
    b = pos[1]    
    
    
  
    
    
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
    
    pygame.display.flip()
    
    
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
