import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (144, 201, 120)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('Sprites/Robot.png').convert_alpha()
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.speed = 5
        self.velocity_y = 0
        self.on_ground = False

    def update(self, pressed_keys, platforms):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        self.rect.move_ip(0, self.speed)
        col = pygame.sprite.spritecollide(self, platforms, False)
        if col:
            self.rect.bottom = col[0].rect.top
            self.velocity_y = 0
        self.on_ground = False
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

player = Player()
platform = Platform(200,20)
platform.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT - 100)
all_sprites = pygame.sprite.Group()
all_sprites.add(player, platform)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, platforms='')

    screen.fill(BG_COLOR)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

