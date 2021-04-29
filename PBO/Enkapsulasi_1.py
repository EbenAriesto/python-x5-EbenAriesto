class Hero:
    jumlah = 0

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getname(self):
        return self.__name
    
    def gethealth(self):
        return self.__health

    def diserang(self, attserang):
        self.__health -= attserang

lina = Hero("Lina", 10)
print(lina.getname())
print(lina.gethealth())
lina.diserang(5)
print(lina.gethealth())