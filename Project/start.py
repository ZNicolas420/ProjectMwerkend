p = 100;
manganaam = input("naam van de manga?")
thema = input("thema?")
genre = input("genre?")
print("naam:" + manganaam + " thema:" + thema + " genre:" + genre)
print("verhaal?")
print("dialoog?")
dialoog = int(input())
print("karakaters?")
karakaters = int(input())
if ((dialoog + karakaters) > p):
    print ("hoer" )
else:
    print("verhaal")
    print(p-(dialoog + karakaters),"%")
