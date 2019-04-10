import pygame


class Mole(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def update(self, position):
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
