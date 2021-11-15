import random
import sys
import pygame
from pygame.locals import QUIT

score_1 = 0
score_2 = 0

pygame.init()
pygame.display.set_caption('SHOOT_GAME')
SURFACE = pygame.display.set_mode((1000, 600))
Big_font = pygame.font.Font('C:\Windows\Fonts\ALGER.TTF', 80)
Small_font = pygame.font.Font('C:\Windows\Fonts\ALGER.TTF', 40)


class Paddle(pygame.Rect):
    def Game_Border():
        Start_Point = [(100, 150), (100, 150), (100, 550), (900, 150)]
        End_Point = [(100, 550), (900, 150), (900, 550), (900, 550)]
        for index in range(len(Start_Point)):
            pygame.draw.line(SURFACE, (255, 255, 255), Start_Point[index], End_Point[index])

    def start():
       # while True:
            #message_Title = Big_font.render("SHOOT_GAME", True, (255, 255, 255))  # 게임제목 적
            #message_game_start = Small_font.render("Game_start : Click the Space_Bar", True, (255, 255, 255))  # 게임시작
       message_Title = Big_font.render("SHOOT_GAME", True, (255, 255, 255))  # 게임제목 적기
       message_caution = Small_font.render("Missile_Button : A , Missile is only one ", True, (255, 255, 255))
       while True:
           SURFACE.fill((0, 0, 0))
           for event in pygame.event.get():
               if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
           SURFACE.blit(message_Title, (350, 20))  # 화면상에 제목 표시
           Paddle.Game_Border()
           pygame.display.update()


    def __init__(self, velocity, up_key, down_key, *args, **kwargs):
        self.velocity = velocity
        self.up_key = up_key
        self.down_key = down_key
        ## self.colour = colour
        super().__init__(*args, **kwargs)

    def move_paddle(self, board_height):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[self.up_key]:
            if self.y - self.velocity > 0:
                self.y -= self.velocity

        if keys_pressed[self.down_key]:
            if self.y + self.velocity < board_height - self.height:
                self.y += self.velocity


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
        pygame.init()  # Start the pygame instance.

        # Setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        # Create the player objects.

        self.paddles = []
        self.balls = []
        self.paddles.append(Paddle(  # The left paddle
            self.BALL_VELOCITY,
            pygame.K_w,
            pygame.K_s,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,
            ##self.colour = (255, 0, 0)

        ))

        self.paddles.append(Paddle(  # The right paddle
            self.BALL_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT,
            ##self.colour = (0, 0, 255)
        ))

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
            for paddle in self.paddles:
                if ball.colliderect(paddle):
                    ball.velocity = -ball.velocity
                    ball.angle = random.randint(-5, 5)
                    break

    def game_loop(self):
        background = pygame.image.load("abc.jpg")
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Add some extra ways to exit the game.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        self.check_ball_hits_paddle()
        self.check_ball_hits_wall()

        # Redraw the screen.
        # self.screen.fill((0, 0, 0))

        for paddle in self.paddles:
            paddle.move_paddle(self.HEIGHT)
            pygame.draw.rect(self.screen, self.COLOUR, paddle)

        # We know we're not ending the game so lets move the ball here.
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

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

  def show_go_screen(self):
      pong = Pong()
      pong.game_loop()

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)


if __name__ == '__main__':
    show_start_screen()
    while g.running:j
        g.new()
        g.show_go_screen()

    pg.quit()
    wait_for_key()

