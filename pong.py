import pygame, sys
from pygame.locals import *
from random import randint

WHITE = (255,255,255)
BLACK = (0,0,0)
window_width = 500
window_height = 500
screen_border = 15
all_paddle_widths = 10
all_paddle_heights = window_height // 10
screen = pygame.display.set_mode((window_width, window_height))
screen.fill(BLACK)
fps_clock = pygame.time.Clock()
fps = 200  

class Paddle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.paddle_rect = pygame.Rect((self.x, self.y), (self.w, self.h))
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.paddle_rect)
        
    def move(self, pos):
        if self.paddle_rect.y > window_height - screen_border // 2 - self.h:
            self.paddle_rect.y = window_height - screen_border // 2 - self.h
        elif self.paddle_rect.y < screen_border // 2:
            self.paddle_rect.y = screen_border // 2
        else:
            self.paddle_rect.y = pos[1] - self.h // 2
        
class ComputerPaddle(Paddle):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.paddle_rect = pygame.Rect((self.x, self.y), (self.w, self.h))
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.paddle_rect)
        
    def move(self, ball):
        rand_num = randint(1,10)
        if self.paddle_rect.y < ball.ball_rect.y:
            if rand_num <= 3:
                self.paddle_rect.y += abs(int(ball.speed[1] * 0.8))
            elif rand_num <= 8:
                self.paddle_rect.y += abs(int(ball.speed[1]))
            else:
                self.paddle_rect.y += abs((ball.speed[1] * 1.2))
        else:
            if rand_num <= 3:
                self.paddle_rect.y -= abs(int(ball.speed[1] * 0.8))
            elif rand_num <= 8:
                self.paddle_rect.y -= abs(int(ball.speed[1]))
            else:
                self.paddle_rect.y -= abs((ball.speed[1] * 1.2))
                
class Ball():
    def __init__(self, x, y, w, h, speed, score):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.score = score
        self.is_moving = False
        self.must_restart = False
        self.ball_rect = pygame.Rect((self.x, self.y), (self.w, self.h))
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.ball_rect)
        
    def move(self):
        if self.hit_top() or self.hit_bottom():
            self.speed[1] = -self.speed[1]
        self.hit_left_check(self.score)
        self.hit_right_check(self.score)
        self.ball_rect.x += self.speed[0]
        self.ball_rect.y += self.speed[1]
        self.is_moving = True
        
    def hit_top(self):
        if self.ball_rect.top < 0:
            return True
        else:
            return False
    
    def hit_bottom(self):
        if self.ball_rect.bottom > window_height:
            return True
        else:
            return False
            
    def hit_right_check(self, score):
        if self.ball_rect.right > window_width:
            score.player_increment()
            self.must_restart = True
            
    def hit_left_check(self, score):
        if self.ball_rect.left < 0:
            score.computer_increment()
            self.must_restart = True
            
    def hit_paddle_check(self, paddle):
        if self.ball_rect.colliderect(paddle.paddle_rect):
            self.speed[0] = -self.speed[0]
            self.move()

    def follow_paddle(self, paddle, pos):
        if self.ball_rect.y < all_paddle_heights // 2 + screen_border // 2 - self.h // 2:
            self.ball_rect.y = all_paddle_heights // 2 + screen_border // 2 - self.h // 2
        elif self.ball_rect.y > window_height - screen_border // 2 - all_paddle_heights // 2:
            self.ball_rect.y = window_height - screen_border // 2 - all_paddle_heights // 2
        else:
            self.ball_rect.y = paddle.paddle_rect.y + paddle.h - all_paddle_heights //2 - self.h // 2
        
class Score():
    def __init__(self, font_size):
        self.font_size = font_size
        self.font = pygame.font.Font(None, self.font_size)
        self.player_score = 0
        self.computer_score = 0
    
    def player_increment(self):
        self.player_score += 1
        
    def computer_increment(self):
        self.computer_score += 1
        
    def draw(self):
        shown_player_score = self.font.render("{}".format(self.player_score), True, WHITE)
        shown_player_rect = shown_player_score.get_rect()
        shown_player_rect.topright = window_width // 2 - 20, 20
        screen.blit(shown_player_score, shown_player_rect)
        
        shown_computer_score = self.font.render("{}".format(self.computer_score), True, WHITE)
        shown_computer_rect = shown_computer_score.get_rect()
        shown_computer_rect.topleft = window_width // 2 + 20, 20
        screen.blit(shown_computer_score, shown_computer_rect)
        
class Engine():
    def __init__(self):
        paddle_x = int(window_width * 1 / 10)
        paddle_y = window_height // 2
        self.paddle = Paddle(paddle_x, paddle_y, all_paddle_widths, all_paddle_heights)
        
        computer_paddle_x = int(window_width * 9 / 10 - all_paddle_widths)
        computer_paddle_y = window_height // 2
        self.computer_paddle = ComputerPaddle(computer_paddle_x, computer_paddle_y, all_paddle_widths, all_paddle_heights)
        
        self.score = Score(30)
        
        ball_length = 10
        ball_width = 10
        self.ball = Ball(paddle_x + all_paddle_widths + 5, window_height // 2 + self.paddle.h // 2 
            - ball_width // 2, ball_length, ball_width, [3,3], self.score)
            
    def draw(self):
        screen.fill(BLACK)
        self.ball.hit_paddle_check(self.paddle)
        self.ball.hit_paddle_check(self.computer_paddle)
        self.paddle.draw()
        self.computer_paddle.draw()
        if self.ball.must_restart == False:
            self.ball.draw()
        pygame.draw.rect(screen, WHITE, ((0,0), (window_width, window_height)), screen_border)
        self.score.draw()
        
        pygame.display.flip()
        
    def restart(self, paddle):
        self.ball = Ball(int(window_width * 1 / 10) + all_paddle_widths + 5, paddle.paddle_rect.y
            + paddle.paddle_rect.h // 2 - screen_border // 2, 10, 10, [3,3], self.score)
        
def main():
    pygame.init()
    pygame.display.set_caption("Pong")
    pygame.mouse.set_visible(0)
    engine = Engine()
    
    while True:
        fps_clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                engine.paddle.move(event.pos)
                if engine.ball.is_moving == False:
                    engine.ball.follow_paddle(engine.paddle, event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                engine.ball.is_moving = True
        if engine.ball.must_restart:
            engine.restart(engine.paddle)
        if engine.ball.is_moving:
            engine.ball.move()
            engine.computer_paddle.move(engine.ball)
        engine.draw()

if __name__=='__main__':
    main()