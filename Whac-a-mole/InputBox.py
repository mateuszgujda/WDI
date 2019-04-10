import pygame
import pygame.locals
import Button
import os


messageButton = Button.Button(os.path.join("data","message_box.png"))

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,38)
  messageButton.update((screen.get_width()/2 -20,screen.get_height()/2 ))
  messageButton.draw(screen)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 220, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  string = ""
  current_string = []
  display_box(screen, question + ": " + string.join(current_string))
  while 1:
    inkey = get_key()
    if inkey == pygame.K_BACKSPACE:
      if(len(current_string) != 0):
        current_string.pop(-1)
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      if(len(current_string)<14):
        current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string))
  return string.join(current_string)