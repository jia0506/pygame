import random
import sys
import pygame

pygame.init()
score_1 = 0
score_2 = 0
Small_font = pygame.font.SysFont('arial', 40)
Big_font = pygame.font.SysFont('arial', 40)

class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


class PaddleAI(pygame.Rect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move_paddle(self, ball_y):
        # keys_pressed = pygame.key.get_pressed()
        if random.randrange(0,50) == 6 :
                self.y = ball_y + 60

        else:
            self.y = ball_y - 40

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 0
        super().__init__(*args, **kwargs)

    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle


class Pong:
    WIDTH = 800
    HEIGHT = 600

    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 100

    BALL_WIDTH = 10
    BALL_VELOCITY = 5
    BALL_ANGLE = 0
    score = 0

    COLOUR = (255, 255, 255)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.paddles1 = Paddle(
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,
        )

        self.paddles2 = PaddleAI(
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,


        )
        self.balls = []

        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))

        self.central_line = pygame.Rect(self.WIDTH / 2, 0, 1, self.HEIGHT)

    def ball_reset(self):
        for ball in self.balls:
            ball.x = self.WIDTH / 2
            ball.y = self.HEIGHT / 2

            print(f'{score_1} : {score_2}')

            ball.velocity = random.choice([5, -5])
            ball.angle = random.randint(-5, 5)
            pygame.time.wait(1000)

    def check_ball_hits_wall(self):
        global score_1, score_2
        for ball in self.balls:
            if ball.x > self.WIDTH:
                score_1 += 1
                pong.ball_reset()
            if ball.x < 0:
                score_2 += 1
                pong.ball_reset()

            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        for ball in self.balls:
            if ball.colliderect(self.paddles1):
                ball.velocity = -ball.velocity
                ball.angle = random.randint(-5, 5)
                break
            if ball.colliderect(self.paddles2):
                ball.velocity = -ball.velocity
                ball.angle = random.randint(-5, 5)
                break

    def game_loop(self):
        while True:
            background = pygame.image.load("abc.jpg")
            background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
            self.screen.blit(background, (0, 0))
            score1=Small_font.render(f'{score_1}',True, (255,255,255))
            score2 = Small_font.render(f'{score_2}', True, (255, 255, 255))
            self.screen.blit(score1,(400-score1.get_width() - 5,10))
            self.screen.blit(score2, (405, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.check_ball_hits_paddle()
            self.check_ball_hits_wall()

            self.paddles1.move_paddle(self.HEIGHT)
            pygame.draw.rect(self.screen,self.COLOUR,self.paddles1)
            for ball in self.balls:
                self.paddles2.move_paddle(ball.y)
                pygame.draw.rect(self.screen,self.COLOUR,self.paddles2)

            for ball in self.balls:
                ball.move_ball()
                pygame.draw.rect(self.screen, self.COLOUR, ball)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                    running = False

            pygame.draw.rect(self.screen, self.COLOUR, self.central_line)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
        pong = Pong()
        pong.game_loop()
