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
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.max_velocity = 5
        self.x_velocity = self.max_velocity
        self.y_velocity = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, [255, 255, 255], [self.x, self.y], self.radius)
    
    def movement(self):
        #Para mover la pelota va a ser en base en que parte de la raqueta haya tocado la pelota
        self.x += self.x_velocity
        self.y += self.y_velocity
        
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= -1 


def draw_score(screen, player_score, x):
    font = pygame.font.SysFont("comicsans", 50)
    score = font.render(str(player_score), True, (255, 255, 255))
    screen.blit(score, (x, 20))

def draw_game(screen, player1, player2, ball, width, height, score_player1, score_player2):
    screen.fill([0, 0, 0])
    draw_score(screen, score_player1, width//4 - 25)
    draw_score(screen, score_player2, width * (3/4) - 25)
    
    player1.draw(screen)
    player2.draw(screen)
    
    ball.draw(screen)
    
    #DRAWING DASH LINE
    for i in range(10, height, height//20):
        if i % 2 == 0:
            pygame.draw.rect(screen, [255, 255, 255], [width//2 -5, i, 10, height//20])
    
    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle, height):
    #Cuando toquemos la parte arriba o abajo cambiamos de dirección
    if ball.y + ball.radius >= height:
        ball.y_velocity *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_velocity *= -1
    
    #LEFT SIDE
    if ball.x_velocity < 0:
        #Vamos a checar que las coordenadas de la pelota sean iguales a las de la raqueta
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height: #Checamos colisione en "y"
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_velocity *= -1
                
                #Velocity for y axis
                paddle_middle_y = left_paddle.y + (left_paddle.height // 2) #Obtenemos la coordenada donde esta el medio de la raqueta
                difference_in_y = paddle_middle_y - ball.y #Checamos la distancia que hay entre la pelota y el medio de la raqueta
                reduction_factor = (left_paddle.height // 2) / ball.max_velocity
                velocity_for_y = difference_in_y // reduction_factor #Obtenemos la velcoidad para "y"
                ball.y_velocity = velocity_for_y * -1
    
    #RIGHT SIDE
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velocity *= -1
                
                #Velocity for y axis
                paddle_middle_y = right_paddle.y + (right_paddle.height // 2) #Obtenemos la coordenada donde esta el medio de la raqueta
                difference_in_y = paddle_middle_y - ball.y #Checamos la distancia que hay entre la pelota y el medio de la raqueta
                reduction_factor = (right_paddle.height // 2) / ball.max_velocity
                velocity_for_y = difference_in_y // reduction_factor #Obtenemos la velcoidad para "y"
                ball.y_velocity = velocity_for_y * -1
                
                print("plank right")
    
    print(f'x velocity: {ball.x_velocity}, x: {ball.x}')


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
    
    ball = Ball(screen_width//2, screen_height//2, 7)
    
    left_score = 0
    right_score = 0
    
    running = True
    while running:
        
        #FRAME RATE
        clock.tick(FPS)
        
        #USER INPUT
        key = pygame.key.get_pressed()
        
        player1.movement(key, -1)
        player2.movement(key, 1)    
        ball.movement()
        
        handle_collision(ball, player1, player2, screen_height)
    
        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > screen_width:
            left_score += 1
            ball.reset()
            
        
        draw_game(screen, player1, player2, ball, screen_width, screen_height, left_score, right_score)
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                running = False
    pygame.quit()
    

if __name__ == '__main__':
    run()
    