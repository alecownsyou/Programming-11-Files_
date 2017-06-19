import pygame
 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (122, 92, 48)
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])
    
def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)

def sum_two_numbers(a, b):
    result = a + b
    return result
pygame.init()
 

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 

done = False
 

clock = pygame.time.Clock()
 

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
 
    screen.fill(WHITE)
    
    sum_two_numbers(22, 15)
    
    my_result = sum_two_numbers(22, 15)
    print(my_result)    
    
    draw_tree(screen, 0, 230)
    draw_tree(screen, 200, 230)
    draw_tree(screen, 400, 230)
    
    
   
    pygame.display.flip()
 
   
    clock.tick(60)
 

pygame.quit()