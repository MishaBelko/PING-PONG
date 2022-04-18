import random
from pygame import *
list = [6,-6]
mixer.init()
#создай окно игры
window = display.set_mode((1600, 900))

display.set_caption('PING-COCK')
win_width = 1600
win_height = 900
#задай фон сцены
background = transform.scale(image.load('back.png'), (1600,900))
mixer.music.load('Wii - Shop Theme.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
game = True
speed = 5
score1 = 0
score2 = 0
display.toggle_fullscreen() 
sp_x = random.choice(list)
sp_y = random.choice(list)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (90, 90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed 

class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed  
run = True
finish = False
clock = time.Clock()
FPS = 144
font.init()
font = font.SysFont('Arial', 70)
player1 = Player2('photo_2022-04-10_13-02-38.jpg', 250, win_height - 200, 12)
player2 = Player1('photo_2022-04-10_13-02-38.jpg', 1250, win_height - 200, 12)
ball = GameSprite('pngegg.png', 800, 450, 2)
cock = mixer.Sound('cock.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False    
    win1 = font.render('Player 1 WIN!', 1, (1, 1, 255))
    win2 = font.render('Player 2 WIN!', 1, (255, 0, 0))
    lose = font.render('GAME OVER!', 1, (0, 255, 0))
    res = font.render('press F5 to restart', 1, (0,255,0))
    ex = font.render('or Q for exit', 1, (0,255,0))
    PS1 = font.render('1 Player ' + str(score1), 1, (0,0,255))
    PS2 = font.render('2 Player ' + str(score2), 1, (255,0,0))
    keys = key.get_pressed()
    if keys[K_F5]:
        finish = False
        ball.rect.x = 800
        ball.rect.y = 450
        mixer.music.load('Wii - Shop Theme.mp3')
        mixer.music.play()
        mixer.music.set_volume(0.1)
        score2 = 0
        score1 = 0 
    if keys[K_ESCAPE]:
        finish = True
    if keys[K_SPACE]:
        finish = False
    if keys[K_q]:
        game = False
    if finish != True:
        window.blit(background,(0, 0))
        ball.rect.x += sp_x
        ball.rect.y += sp_y
        if sprite.collide_rect(player1, ball):
            sp_x *= -1
            cock.play()
            score1 += 1
        if sprite.collide_rect(player2, ball):
            sp_x *= -1
            cock.play()
            score2 += 1
        if ball.rect.y > win_height-120 or ball.rect.y < 0:
            sp_y *= -1
            cock.play()
        if ball.rect.x < 0 or ball.rect.x > 1500:
            mixer.music.load('win.ogg')
            mixer.music.play()
            window.blit(lose, (600,400))
            window.blit(res, (560,460))
            window.blit(ex, (610, 520))
            finish = True
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        window.blit(PS1, (20,20))
        window.blit(PS2, (1300,20))
        display.update()
        clock.tick(FPS)