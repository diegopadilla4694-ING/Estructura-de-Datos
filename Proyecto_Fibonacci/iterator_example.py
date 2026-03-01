class Num:
    def __init__(self, character):
        self.__n = character
        self.__cont = 0
        self.__p1 = self.__p2 = 1
    
    def __iter__(self):
        print("Use __iter__")
        return self
    
    def __next__(self):
        self.__cont += 1
        if self.__cont > self.__n:
            raise StopIteration
        if self.__cont in [1, 2]:
            return 1        
        
        Total = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, Total
        return Total


class Suma:
    def __init__(self, num):
        self.___iter = Num(num)
    
    def __iter__(self):
        print("Class Suma in Action")
        return self.__iter
    
object = Num(10)

for value in object:
    print(value)