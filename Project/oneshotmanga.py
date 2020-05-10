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

        print("verhaal    :" , self.dialoog ,"%", self.karakaters ,"%", self.verhaal,"%")
        print("tekeningen :" , self.achtergronden ,"%", self.persoonage ,"%", self.effecten,"%")

o1 = Oneshotmanga("tuto", "avontuur", "zombie",50,50,50,50,50,50)


o1.introduce_self()
