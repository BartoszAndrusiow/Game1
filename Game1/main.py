from datetime import date
import datetime
import pygame
from fruit import Fruit
import snake;
from directorEnum import DirectoryEnum;

#Draw All Fruits
def DrawAllFruits(pygame, screen, allFruits):
    imp = pygame.image.load(".\\Image\\apple.png").convert()

    for fruit in allFruits:
        pygame.draw.rect(screen,fruit.GetColor(),pygame.Rect(fruit.GetPosition()))
        screen.blit( imp,pygame.Rect(fruit.GetPosition()));

#snake consume Fruit
def SnakeConsumeFruit(snake, allFruits):
    for i in range(0, len(allFruits) - 1 ):
        if(snake.GetX()< allFruits[i].GetX() + allFruits[i].GetSize() and
           snake.GetX() +snake.GetSize() > allFruits[i].GetX() and
           snake.GetY() < allFruits[i].GetY()+ allFruits[i].GetSize() and
           snake.GetY() + snake.GetSize() > allFruits[i].GetY()):
            allFruits.pop(i);
            snake.SpeedUp();
# pygame setup
window_h = 800;
window_w = 600;
pygame.init()
screen = pygame.display.set_mode((window_h, window_w))
clock = pygame.time.Clock()
running = True
maxFruits = 4;

color = (255,0,0)
speed = 1;
newFruitTime = 10;
snake = snake.Snake();

current_dateTime = datetime.datetime.now()  

allFruits =[];

horisMoves = (DirectoryEnum.DirectorLEFT,DirectoryEnum.DirectorRIGHT)
verticalMoves = (DirectoryEnum.DirectorDown,DirectoryEnum.DirectorUp)
while running:
    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check key down
        elif event.type == pygame.KEYDOWN:
            screen.fill(0)
            if event.key == pygame.K_LEFT and snake.GetDirect() not in horisMoves:
                snake.AddMoves(snake.x, snake.y)
                newX = snake.GetX() - snake.GetSpeed();
                snake.SetPosition(newX, snake.GetY());
                snake.SetDirect(DirectoryEnum.DirectorLEFT);
            elif event.key == pygame.K_RIGHT and snake.GetDirect() not in horisMoves:
                snake.AddMoves(snake.x, snake.y)
                newX = snake.GetX() + snake.GetSpeed();
                snake.SetPosition(newX, snake.GetY());
                snake.SetDirect(DirectoryEnum.DirectorRIGHT);
            elif event.key == pygame.K_UP and snake.GetDirect() not in verticalMoves:
                snake.AddMoves(snake.x, snake.y)
                newY =  snake.GetY() - snake.GetSpeed();
                snake.SetPosition(snake.GetX(), newY);
                snake.SetDirect(DirectoryEnum.DirectorUp);
            elif event.key == pygame.K_DOWN and snake.GetDirect() not in verticalMoves:
                snake.AddMoves(snake.x, snake.y)
                newY =  snake.GetY() + snake.GetSpeed();
                snake.SetPosition(snake.GetX(), newY);
                snake.SetDirect(DirectoryEnum.DirectorDown);

    #Move snake
    if snake.GetDirect() == DirectoryEnum.DirectorRIGHT:
        newX = snake.GetX() + snake.GetSpeed();
        snake.SetPosition(newX, snake.GetY());
    if snake.GetDirect() == DirectoryEnum.DirectorLEFT:
        newX = snake.GetX() - snake.GetSpeed();
        snake.SetPosition(newX, snake.GetY());
    if snake.GetDirect() == DirectoryEnum.DirectorDown:
        newY =  snake.GetY() + snake.GetSpeed();
        snake.SetPosition(snake.GetX(), newY);
    if snake.GetDirect() == DirectoryEnum.DirectorUp:
        newY =  snake.GetY() - snake.GetSpeed();
        snake.SetPosition(snake.GetX(), newY);
    #check edge
    if snake.GetY()>window_w or snake.GetX()> window_h:
        running = False;
    if snake.GetY()<0 or snake.GetX()< 0:
        running = False;
    
    newNow = datetime.datetime.now() ;
    if (newNow - current_dateTime).total_seconds() > newFruitTime and len(allFruits) < maxFruits:
        current_dateTime = newNow;
        allFruits.append(Fruit(window_h, window_w))
    screen.fill(0)
    # fill the screen with a color to wipe away anything from last frame
    DrawAllFruits(pygame, screen, allFruits);
    SnakeConsumeFruit(snake, allFruits);
    pygame.draw.rect(screen, color, pygame.Rect(snake.GetPosition()))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()