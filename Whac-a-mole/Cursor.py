import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def hit(self, target):
        return self.rect.colliderect(target)

    def update(self, position):
        self.rect.topleft = position

    def draw(self,screen):
        screen.blit(self.image, self.rect)

