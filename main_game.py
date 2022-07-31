import pygame
pygame.init()
print("!-start")

size = (800, 500)
screen = pygame.display.set_mode(size)
runing = True

text  = open("Plays_list.txt", "r")
lines = text.readline()
print("!-txt opened")
#loads the image
button_img = pygame.image.load("Button.png").convert_alpha()

clock = pygame.time.Clock()

class Button():
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.click = False


    def draw(self):

        action = False

        #gets the mouse postitions
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):

            #checks if the mouse is cliked
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                action = True
                
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

        screen.blit(self.img, (self.rect.x, self.rect.y))
        
        return action

print("!-Class defined")
main_button = Button(400, 250, button_img)
print("!-entering main loop")
waiting = True


while runing:

    clock.tick(30)

    screen.fill((255, 255, 255))
    main_button.draw()
    pygame.display.update()
    for line in lines:
        waiting = True
        while waiting:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    runing = False
        
            if main_button.draw():
                print("Cliked!")
                print(line)
                
                waiting = False


pygame.quit()
