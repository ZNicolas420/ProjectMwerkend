genre = "Action"
thema = "Cyberpunk"




def Cyberpunk():
    print("%vanhoe goed het samen werkt en de top score per type")


def Action(thema):
    switcher = {
        "Cyberpunk": Cyberpunk(),
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }




def checkgenre(genre):
    switcher = {
        "Action": Action(thema),
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve
    }


checkgenre(genre)
