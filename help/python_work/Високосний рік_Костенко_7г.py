#програма високосний рік
#вхідні дані: рік
#вихідні дані: чи цей рік високосний: так, ні
#Костенко Іван, 7г

year=int(input("Введіть рік "))
if (year%4==0):
    print("ТАК")
else:
    print("НІ")