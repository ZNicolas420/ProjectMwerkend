from oneshotmanga import Oneshotmanga


def berekenprocent(a,b,c):
    totaal = a+b+c
    round((a/totaal)*100)
    return(round((a/totaal)*100))




manganaam = input("naam van de manga?")
thema = input("thema?")
genre = input("genre?")
print("dialoog?")
dialoog = int(input())
print("karakaters?")
karakaters = int(input())
print("verhaal?")
verhaal = int(input())
print("----------------------------------------------------------------------------------------------------------------------")
print("achtergronden-?")
achtergronden = int(input())
print("persoonage-?")
persoonage = int(input())
print("effecten?")
effecten = int(input())
print("----------------------------------------------------------------------------------------------------------------------")
o1 = Oneshotmanga(manganaam,thema,genre,dialoog,karakaters,verhaal,achtergronden,persoonage,effecten)
print("----------------------------------------------------------------------------------------------------------------------")
o1.introduce_self()
