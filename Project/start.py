def berekenprocent(a,b,c):
    totaal = a+b+c
    round((a/totaal)*100)
    return(round((a/totaal)*100))

p = 100;
manganaam = input("naam van de manga?")
thema = input("thema?")
genre = input("genre?")
print("naam:" + manganaam + " thema:" + thema + " genre:" + genre)
print("dialoog?")
dialoog = int(input())
print("karakaters?")
karakaters = int(input())
print("verhaal?")
verhaal = int(input())
print("----------------------------------------------------------------------------------------------------------------------")
print("dialoog :" , berekenprocent(dialoog,karakaters,verhaal),"%")
print("karakaters :" , berekenprocent(karakaters,dialoog,verhaal),"%")
print("verhaal :" , berekenprocent(verhaal,karakaters,dialoog),"%")
