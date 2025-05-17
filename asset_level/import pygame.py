import pygame
pygame.init() # запускаем модули pygame
wind = pygame.display.set_mode((1000, 700)) # окно игри
clock = pygame.time.Clock() # часи для управления кадрами в секунду

class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width # метод ширина
        self.height = height # метод длина
        self.color = color # метод цвет
        self.rec = pygame.Rect(self.x,self.y,self.width,self.height)
    def draw2(self):
        pygame.draw.rect(wind,self.color, self.rec)

with open("r.txt", "r") as file: # откриваем файл, считиваем 
    data = file.readlines() # сохраняем 
class Ball: # клас шарики 
    def __init__(self , x,y, color, radius): # конструктор параметри
        self.x = x # сохраняем координати шарика
        self.y = y # сохраняем координати шарика
        self.radius = radius # сохраняем радиус
        self.color = color # сохраняем цвет
        self.speed_x = 2 # устанавливаем скорость по горизонтали
        self.speed_y = 2# устанавливаем скорость по вертикали



    def draww(self): # рисует круг
        pygame.draw.circle(wind,self.color, (self.x, self.y), self.radius)
    def go(self): # движение шара
        # self.x += 2 # двигаем на 2 пикселя по горизонтали 
        # self.y += 2 # двигаем на 2 пикселя по вертикали
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 670: # движение с учетом скорости
            self.speed_y *= -1
        if self.x > 670: # движение с учетом скорости
            self.speed_x *= -1
        if self.y < 0:
            self.speed_y *= -1

        if self.x < 0:
            self.speed_x *= -1

       


ball = Ball(200, 200 ,(0,200,100), 35) # создаем мяч 
CR2 = Ball(50, 150 ,(255,255,255), 50,) # создаем мяч
o = []
a = []
for i in enumerate(data):
   for index, char in enumerate(): 
        for index,char in enumerate(data):
            if char == "#":

                block1 = Block(index*100,100,50,50, (255,145,15))
                block2 = Block(index*100,100,50,50, (255,145,15))
        a.append(block1)
        o.append(block2)


game = 1 # пока game = 1 цикл будет роботать
while game:
    wind.fill((0,0,0)) # очищаем екран черним цветом
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (1000, 0), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (0, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 700), (1000, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (1000, 0), (1000, 700), 5)

for i in enumerate(data):
   for index, char in enumerate(): 


    # обработка собития для закрития окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
            pygame.quit()

    ball.go() # двигаем мячик
    ball.draww() # рисуем мячик
    CR2.go()
    CR2.draww()

    for i in a:
        i.draw2()
    for i in o:
        i.draw2()

    

    
    
    

    pygame.display.update() # обновляем екран чтоби все отрисовалось
    clock.tick(60) # ограничиваем кадри в секунду