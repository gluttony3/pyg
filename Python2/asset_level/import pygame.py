import pygame
pygame.init()
wind = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()



with open("r.txt", "r") as file:
    data = file.read()
class Ball:
    def __init__(self , x,y, color, radius):
        self.x = x

        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 1
        self.speed_y = 1



    def draww(self):
        pygame.draw.circle(wind,self.color, (self.x, self.y), self.radius)
    def go(self):
        self.x += 2
        self.y += 2
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 670:
            self.speed_y *= -1
            

ball = Ball(200, 200 ,(0,200,100), 35)
CR2 = Ball(50, 150 ,(255,255,255), 50,)

game = 1
while game:
    wind.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
            pygame.quit()

    ball.go()
    ball.draww()
    CR2.go()
    CR2.draww()
    
    for index, char in enumerate(data):
        if char == "#":
            pygame.draw.rect(wind, (255,255,255), (index*100,500, 70, 50))

    pygame.display.update()
    clock.tick(60)