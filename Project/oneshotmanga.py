class Oneshotmanga:
    def __init__(self,manganaam,thema,genre,dialoog, karakaters,verhaal,achtergronden,persoonage,effecten):
        self.manganaam = manganaam
        self.thema = thema
        self.genre = genre
        self.dialoog = dialoog
        self.karakaters = karakaters
        self.verhaal = verhaal
        self.achtergronden = achtergronden
        self.persoonage = persoonage
        self.effecten = effecten
    def introduce_self(self):
        print("Naam  : " + self.manganaam)
        print("thema : " + self.thema)
        print("genre : " + self.genre)

        print("verhaal    :" , berekenprocent(self.dialoog,self.karakaters,self.verhaal) ,"%", berekenprocent(self.karakaters,self.dialoog,self.verhaal) ,"%", berekenprocent(self.verhaal,self.dialoog,self.karakaters),"%")
        print("tekeningen :" , berekenprocent(self.achtergronden,self.persoonage,self.effecten) ,"%", berekenprocent(self.persoonage,self.achtergronden,self.effecten) ,"%", berekenprocent(self.effecten,self.achtergronden,self.persoonage),"%")

def berekenprocent(a,b,c):
    totaal = a+b+c
    round((a/totaal)*100)
    return(round((a/totaal)*100))

#manga maken/save info
#o1 = Oneshotmanga("tuto", "avontuur", "zombie",50,50,50,50,50,50)

#manga gegevens opvragen
#o1.introduce_self()


#berekenprocent(self.effecten,self.achtergronden,self.persoonage)
