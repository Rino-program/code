import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer Game")

# Clock
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 70)
        self.vel_y = 0
        self.jumping = False

    def update(self):
        self.vel_y += GRAVITY
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE] and not self.jumping:
            self.vel_y = -12
            self.jumping = True

        self.rect.y += self.vel_y

        # Collision with ground
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.jumping = False

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed = -self.speed

# Item class
class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def collect(self):
        # Create a simple animation
        for _ in range(5):
            self.image.fill((255, 255, 255))
            screen.blit(self.image, self.rect.topleft)
            pygame.display.flip()
            pygame.time.wait(50)
            self.image.fill(YELLOW)
            screen.blit(self.image, self.rect.topleft)
            pygame.display.flip()
            pygame.time.wait(50)

# Goal class
class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
items = pygame.sprite.Group()
goals = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
platform_list = [
    (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Ground platform
    (150, 450, 200, 20),
    (400, 350, 200, 20),
    (650, 250, 100, 20)
]
for plat in platform_list:
    p = Platform(*plat)
    all_sprites.add(p)
    platforms.add(p)

# Create enemies
for i in range(2):
    e = Enemy(random.randint(0, SCREEN_WIDTH - 50), random.randint(100, SCREEN_HEIGHT - 70), 50, 50)
    all_sprites.add(e)
    enemies.add(e)

# Create items
for i in range(3):
    it = Item(random.randint(0, SCREEN_WIDTH - 30), random.randint(100, SCREEN_HEIGHT - 30), 30, 30)
    all_sprites.add(it)
    items.add(it)

# Create goal
goal = Goal(SCREEN_WIDTH - 70, 200, 50, 50)
all_sprites.add(goal)
goals.add(goal)

# Main game loop
running = True
score = 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Collision detection with platforms
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.rect.y = hits[0].rect.top - player.rect.height
        player.vel_y = 0
        player.jumping = False

    # Collision detection with enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        running = False  # End the game on collision with an enemy

    # Collision detection with items
    collected_items = pygame.sprite.spritecollide(player, items, True)
    if collected_items:
        for item in collected_items:
            item.collect()
        score += len(collected_items)

    # Collision detection with goal
    if pygame.sprite.spritecollide(player, goals, False):
        running = False  # End the game on reaching the goal
        print("You Win! Score:", score)

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    # Refresh screen
    pygame.display.flip()

pygame.quit()