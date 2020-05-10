def berekenprocent(a,b,c):
    totaal = a+b+c
    andernaam = round((a/totaal)*100)
    print(andernaam,"%")

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
print("dialoog :" , format(berekenprocent(dialoog,karakaters,verhaal)))
berekenprocent(karakaters,dialoog,verhaal)
berekenprocent(verhaal,karakaters,dialoog)
