import pygame
import random
import os

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
)

pygame.font.init()

WIDTH, HEIGHT = 500, 500

# Load Images
SNAKE_HEAD = pygame.transform.scale(pygame.image.load(os.path.join("red-square.png")), (20, 20))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join("green-square.png")), (20, 20))
BOMB = pygame.transform.scale(pygame.image.load(os.path.join("blue-square.png")), (20, 20))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Snake(pygame.sprite.Sprite):

    def __init__(self, x, y, width=20, height=20):
        super(Snake, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surf = SNAKE_HEAD.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, WIDTH - 20),
                random.randint(40, HEIGHT - 20)
            )
        )

    # move the sprite based on user key presses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        # keep player within screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def get_width(self):
        return self.surf.get_width()


class Apple(pygame.sprite.Sprite):

    def __init__(self, x, y, width=20, height=20):
        super(Apple, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surf = APPLE.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, WIDTH - 20),
                random.randint(40, HEIGHT - 20)
            )
        )


class Bomb(pygame.sprite.Sprite):

    def __init__(self, x, y, width=20, height=20):
        super(Bomb, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surf = BOMB.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(20, WIDTH - 20),
                random.randint(40, HEIGHT - 40)
            )
        )


def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)
    score = 0

    snake = Snake(250, 250)
    apples = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(snake)

    lost = False

    def redraw_window():
        screen.fill((0, 0, 0))

        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        screen.blit(score_label, (10, 10))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        pygame.display.update()


    while running:
        clock.tick(FPS)
        redraw_window()

        if pygame.sprite.spritecollideany(snake, apples):
            new_apple.kill()
            score += 10
            new_bomb = Bomb(random.randint(20, WIDTH - 20), random.randint(50, HEIGHT - 20))
            bombs.add(new_bomb)
            all_sprites.add(new_bomb)

        if pygame.sprite.spritecollideany(snake, bombs):
            lost = True

        if lost:
            break

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if not apples:
                new_apple = Apple(random.randrange(20, WIDTH - 20), random.randrange(0, HEIGHT - 20), 20, 20)
                apples.add(new_apple)
                all_sprites.add(new_apple)

        keys = pygame.key.get_pressed()
        snake.update(keys)

        apples.update()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 30)
    run = True

    while run:
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        screen.blit(title_label, ((WIDTH / 2) - title_label.get_width() / 2, 200))
        title_label_1 = title_font.render("Eat the apple and be careful of blue bombs...", 1, (255, 255, 255))
        screen.blit(title_label_1, ((WIDTH / 2) - title_label_1.get_width() / 2, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()


main_menu()

pygame.quit()
