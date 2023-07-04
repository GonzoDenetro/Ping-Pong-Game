import pygame
pygame.init()


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.color = [255, 255, 255]
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])
    
    def movement(self, userInput, orientation):
        #We move our paddles depeding the orientation
        if orientation == 1:
            if userInput[pygame.K_UP] and self.y > 5:
                self.y -= self.speed
                print("Arriba")
            elif userInput[pygame.K_DOWN] and self.y + self.height < 495:
                self.y += self.speed
                print("abajao")
        elif orientation == -1:
            if userInput[pygame.K_w] and self.y > 5:
                self.y -= self.speed
                print("Arriba")
            elif userInput[pygame.K_s] and self.y + self.height < 495:
                self.y += self.speed
                print("abajao")
                

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = 5
        self.y_velocity = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], [self.x, self.y], self.radius)


def draw_game(screen, player1, player2, width, height):
    screen.fill([0, 0, 0])
    player1.draw(screen)
    player2.draw(screen)
    
    #DRAWING DASH LINE
    for i in range(10, height, height//20):
        if i % 2 == 0:
            pygame.draw.rect(screen, [255, 255, 255], [width//2 -5, i, 10, height//20])
    
    pygame.display.update()



def run():
    
    #SCREEN SETUP
    screen_width = 700
    screen_height = 500
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Pong Game")
    
    #FPS
    clock = pygame.time.Clock()
    FPS = 60

    player1 = Paddle(10, screen_height//2 - 100//2, 20, 100)
    player2 = Paddle(screen_width - 30, screen_height//2 - 100//2, 20, 100)
    
    running = True
    while running:
        
        #FRAME RATE
        clock.tick(FPS)
        
        #USER INPUT
        key = pygame.key.get_pressed()
        
        player1.movement(key, -1)
        player2.movement(key, 1)    
        
        draw_game(screen, player1, player2, screen_width, screen_height)
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                running = False
    pygame.quit()
    

if __name__ == '__main__':
    run()
    