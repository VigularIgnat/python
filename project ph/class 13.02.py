class Тварини:
    кількість_кінцівок=4
    шкіряний_покрив="шерсть"
    def кінцівки(self,n):
        self.кількість_кінцівок=n
    def покрив (self, p):
        self.шкіряний_покрив=p
    def yce(self,o):
        self.очі=o
    def run(self,r):
        self.run=r
    def heart(self,h):
        self.hurt=h
Собака=Тварини()
Павук=Тварини()
Таракан=Тварини()
Собака.yce(2)
Собака.покрив("шерсть")
Таракан.yce(2)
Таракан.run("по землі")
Собака.run("по землі")
Павук.run("по суходолу")
Таракан.heart(2)
Собака.heart(4)
Павук.heart(1)
print("У собаки є", Собака.кількість_кінцівок, "кінцівки та", Собака.шкіряний_покрив,"та очей", Собака.очі)
Павук.кінцівки(10)
Таракан.кінцівки(15)
Таракан.покрив("луска")
print("У таракана є", Таракан.кількість_кінцівок,"лапок", Таракан.шкіряний_покрив, "має очей", Таракан.очі)
print("У павука", Павук.кількість_кінцівок, "лапок")
print("Таракани ходять ",Таракан.run,"собаки ходять ", Собака.run, "Павуки", Павук.run)
print("У павука серце ",Таракан.hurt,"камерне")
