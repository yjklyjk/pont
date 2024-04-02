class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bsck = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_node((win_width,win_height))

game = True
finish = False
clock = time.Clock()

racket1 = GameSprite('racket.png', 30, 200, 4, 50, 150)
racket2 = GameSprite('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:
            window.fill(bsck)
            racket1.reset()
            racket2.reset()
            ball.reset()

        display.update()
        clock.tick(60)


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15,20,15)
        bullets.add(bullet)


