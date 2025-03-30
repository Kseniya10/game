from pygame import*

width = 700
height = 500
window = display.set_mode((700,500))
display.set_caption("Лабиринт")

background = transform.scale(image.load("background.jpg"),(700,500))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def run(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < height - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def run(self):
        if self.rect.x < 500:
            self.direction = 'right'
        if self.rect.x >= width - 40:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

hero = Player('hero.png', 5, height - 80, 10)
enemy = Enemy('cyborg.png', width - 80, 200, 10)
gold = GameSprite('treasure.png', width - 120, height - 80, 0)

game = True 
finish = False
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if  finish != True:
        window.blit(background,(0,0))
        hero.reset()
        enemy.reset()
        gold.reset()

        hero.run()
        enemy.run()
    display.update()
    clock.tick(FPS)



