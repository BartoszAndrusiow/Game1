import random


class Fruit:
    def __init__(self,max_h,max_w):
        self.x = 0;
        self.y = 0;
        self.__size = 40;
        self.max_h = max_h;
        self.max_w = max_w;
        self.maxColor = 255;
        self.__minPos = 40;
        self.color = (random.randrange(20,self.maxColor-self.__size),random.randrange(20,self.maxColor-self.__size),random.randrange(20,self.maxColor-self.__size))
        self.x = random.randrange(self.__minPos,max_w)
        self.y = random.randrange(self.__minPos,max_h)
    def GetX(self):
        return self.x;
    def GetY(self):
        return self.y;
    def GetColor(self):
        return self.color;
    def GetPosition(self):
        return (self.x, self.y, self.__size, self.__size);
    def GetSize(self):
        return self.__size;