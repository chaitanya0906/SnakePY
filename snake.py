from pygame.locals import *
from random import randint
import pygame
import time
 
class Snake():
    """docstring for Snake"""
    def __init__(Self):
        Self.position=[100,50]
        Self.body=[[100,50],[90,50],[80,50]]
        Self.direction="RIGHT"
        Self.changedirection=Self.direction

    def  changedirto(Self,dir):

        if dir=="RIGHT" and not Self.direction=="LEFT":
            Self.direction="RIGHT"
        if dir=="LEFT" and not Self.direction=="RIGHT":
            Self.direction="LEFT"
        if dir=="UP" and not Self.direction=="DOWN":
            Self.direction="UP"
        if dir=="DOWN" and not Self.direction=="UP":
            Self.direction="DOWN"
        
    def move(Self,foodpos):
        
        if Self.direction =="RIGHT":
            Self.position[0]+=10

        if Self.direction =="LEFT":
            Self.position[0]-=10

        if Self.direction =="UP":
            Self.position[1]-=10

        if Self.direction =="DOWN":
            Self.position[1]+=10

        Self.body.insert(0,Self.position[:])
        
        if Self.position == foodpos:
            return 1
        
        else:
            Self.body.pop()
            return 0

    def checkCollision(Self):
        
        for bodyPart in Self.body[1:]:
            if Self.position== bodyPart:
                return 1
        if Self.position[0] > 490 or Self.position[0] <0:
            Self.position[0]=(Self.position[0]+500)%500

        elif Self.position[1]>490 or Self.position[1]<0:
            Self.position[1]=(Self.position[1]+500)%500
            

        return 0
    def getHeadpos(Self):
        return Self.position

    def getbody(Self):
        return Self.body


class FoodSpawer():
    def __init__(Self):
        Self.position = [100,randint(1,50)*10]
        Self.isFoodOnScreen=  True

    def  spawnfood(Self):
        if Self.isFoodOnScreen  == False:
            Self.position=[randint(1,50)*10,randint(1,50)*10]
            Self.isFoodOnScreen=True

        return Self.position

    def setFoodonScreen(Self,b):
        Self.isFoodOnScreen=b    


window= pygame.display.set_mode((500,500))
pygame.display.set_caption("SNEKS")
fps =  pygame.time.Clock()

score=0

snake= Snake()
foodSpawer= FoodSpawer()

def gameOver():
    pygame.quit()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver()
        elif event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake.changedirto('RIGHT')

            if event.key==pygame.K_UP:
                snake.changedirto('UP')

            if event.key==pygame.K_DOWN:
                snake.changedirto('DOWN')
            
            if event.key==pygame.K_LEFT:
                snake.changedirto('LEFT')

    foodpos = foodSpawer.spawnfood()
    if snake.move(foodpos)==1:
        score+=1
        foodSpawer.setFoodonScreen(False)


    window.fill(pygame.Color(225,225,225))

    for pos in snake.getbody():
        pygame.draw.rect(window,pygame.Color(0,225,0),pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodpos[0],foodpos[1],10,10))

    if(snake.checkCollision()==1):
        gameOver()
    
    pygame.display.set_caption("Wow Snake | Score :" +str(score))
    pygame.display.flip()
    fps.tick(24)



