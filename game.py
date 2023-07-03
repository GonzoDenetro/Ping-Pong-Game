import pygame
pygame.init()

def run():
    
    #SCREEN SETUP
    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.display.set_caption("Pong Game")
    
    #FPS
    clock = pygame.time.Clock()
    FPS = 60
    
    running = True
    while running:
        
        #FRAME RATE
        clock.ticks(60)
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                running = False
    pygame.quit()
    

if __name__ == '__main__':
    run()
    