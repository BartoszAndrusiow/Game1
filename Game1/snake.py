

from directorEnum import DirectoryEnum


class Snake:
    def __init__(self):
        self.x = 150;
        self.y = 50;
        self.__size = 40;
        self.direct = DirectoryEnum.DirectorRIGHT;
        self.__speed = 1;
        self.__SnakeSpeed = 0.5;
        self.__moves =[];
    def GetPosition(self):
        return (self.x, self.y, self.__size, self.__size);
    def SetPosition(self, x, y):
        self.x = x;
        self.y = y;
    def GetX(self):
        return self.x;
    def GetY(self):
        return self.y;
    def SetDirect(self, direct):
        if direct in (1,2,3,4):
            self.direct = direct;
        else:
            raise Exception();
    def GetDirect(self):
        return self.direct;
    def GetHead(self):
        return (self.x +self.__size/2,self.y +self.__size/2)
    def GetSize(self):
        return self.__size;
    def GetSpeed(self):
        return self.__speed;
    def SpeedUp(self):
        self.__speed += self.__SnakeSpeed; 
    def AddMoves(self,x,y):
        self.__moves.append((x,y));