#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_hight, player_wight):
        super().__init__()
        self.hight = player_hight
        self.wight = player_wight
        self.image = transform.scale(image.load(player_image), (self.hight,self.wight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0

bullets = sprite.Group()
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
    
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 10,  20, 15)
        bullets.add(bullet)

lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            lost = lost + 1
        

rocket = Player('rocket.png', 300, 440, 10, 50, 70)
monster = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)
monster2 = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)
monster3 = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)
monster4 = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)
monster5 = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)

monsters = sprite.Group()
monsters.add(monster)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

asteroid = Asteroid('asteroid.png', randint(5, 640), 0, randint(1, 5), 70, 50)
asteroid2 = Asteroid('asteroid.png', randint(5, 640), 0, randint(1, 5), 70, 50)
asteroid3 = Asteroid('asteroid.png', randint(5, 640), 0, randint(1, 5), 70, 50)
asteroid4 = Asteroid('asteroid.png', randint(5, 640), 0, randint(1, 5), 70, 50)
asteroid5 = Asteroid('asteroid.png', randint(5, 640), 0, randint(1, 5), 70, 50)

asteroids = sprite.Group()
asteroids.add(asteroid)
asteroids.add(asteroid2)
asteroids.add(asteroid3)
asteroids.add(asteroid4)
asteroids.add(asteroid5)

font.init()
font2 = font.Font("Arial", 35)

font.init()
font = font.Font("Arial", 35)

clock = time.Clock()
FPS = 60
game = True
finish = False
hit = 0

num_fire = 0
real_time = True
while game:
    window.blit(background,(0, 0))

    keys_pressed = key.get_pressed()
    
    for e in event.get():
        if e.type == QUIT:
            game = False


    
    if finish != True:
        rocket.reset()
        rocket.update()

        monsters.update()
        monsters.draw(window)

        asteroids.update()
        asteroids.draw(window)
               
        bullets.update()
        bullets.draw(window)

        if keys_pressed[K_SPACE]:
            #if num_fire < 10  and not real_time:
            rocket.fire()
            fire.play()
            #num_fire += 1


        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for s in sprites_list:
            hit += 1
            monster = Enemy('ufo.png', randint(5, 640), 0, randint(1, 5), 70, 50)
            monsters.add(monster)
        

        

    text_lose = font2.render("Пропущено:" + str(lost), 1, (255,255,255))
    window.blit(text_lose,(0, 50))
    text_hit = font.render("Попадание:" + str(hit), 1, (255,255,255))
    window.blit(text_hit,(0, 10))

    clock.tick(FPS)

    display.update()