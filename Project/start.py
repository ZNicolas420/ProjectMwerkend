from oneshotmanga import Oneshotmanga



print("1-vulin 2-autovulin")
i = int(input())
if (i==1):
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
elif (i==2):
    o1 = Oneshotmanga("tuto", "avontuur", "zombie",50,50,50,50,50,50)
    o1.introduce_self()
