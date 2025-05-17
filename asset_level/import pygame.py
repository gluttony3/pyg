import pygame
pygame.init() # запускаем модули pygame
wind = pygame.display.set_mode((1000, 700)) # окно игри
clock = pygame.time.Clock() # часи для управления кадрами в секунду



with open("r.txt", "r") as file: # откриваем файл, считиваем 
    data = file.read() # сохраняем 
class Ball: # клас шарики 
    def __init__(self , x,y, color, radius): # конструктор параметри
        self.x = x # сохраняем координати шарика
        self.y = y # сохраняем координати шарика
        self.radius = radius # сохраняем радиус
        self.color = color # сохраняем цвет
        self.speed_x = 1 # устанавливаем скорость по горизонтали
        self.speed_y = 1# устанавливаем скорость по вертикали



    def draww(self): # рисует круг
        pygame.draw.circle(wind,self.color, (self.x, self.y), self.radius)
    def go(self): # движение шара
        self.x += 2 # двигаем на 2 пикселя по горизонтали 
        self.y += 2 # двигаем на 2 пикселя по вертикали
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y > 670: # движение с учетом скорости
            self.speed_y *= -1
            

ball = Ball(200, 200 ,(0,200,100), 35) # создаем мяч 
CR2 = Ball(50, 150 ,(255,255,255), 50,) # создаем мяч 

game = 1 # пока game = 1 цикл будет роботать
while game:
    wind.fill((0,0,0)) # очищаем екран черним цветом
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (1000, 0), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 0), (0, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (0, 700), (1000, 700), 5)
    pygame.draw.line(wind, (255, 0, 0), (1000, 0), (1000, 700), 5)


    # обработка собития для закрития окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = 0
            pygame.quit()

    ball.go() # двигаем мячик
    ball.draww() # рисуем мячик
    CR2.go()
    CR2.draww()
    
    for index, char in enumerate(data): # перебираем все символи из файла r.txt
        if char == "#": # если сивол = # 
            pygame.draw.rect(wind, (255,255,255), (index*100,500, 70, 50)) # рисуеться блок 

    pygame.display.update() # обновляем екран чтоби все отрисовалось
    clock.tick(60) # ограничиваем кадри в секунду