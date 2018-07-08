# Game about building a village
from customprint import print
from random import randint

class Person:

    def __init__(self, name="Sebastian", stats=[], items=[]):

        if stats == []:
            self._stats = [randint(3,9), randint(3,9), randint(3,9), randint(3,9), randint(3,9), randint(3,9)]
        else:
            self._stats = [3, 3, 3, 3, 3, 3]

        self._name = name

    def giveStrList(self):
        printlist = []
        printlist.append(self._name)
        printlist.append("")
        printlist += strFromTwoLists(self._attribute, self._stats)
        return printlist


    _attribute = ["Stärke", "Geschick", "Konstitution", "Weisheit", "Charisma", "Intelligenz"]


def strFromTwoLists(firstList, secondList):
    result = []
    for i in range(len(firstList)):
        result.append(str(firstList[i]) + " - " + str(secondList[i]))
    return result


#Anfangswerte
einwohnerAnzahl = 2
statschar1 = [randint(3,9), randint(3,9), randint(3,9), randint(3,9), randint(3,9), randint(3,9)]


aktivitaeten = ["Farmen", "Bergbau", "Brauen", "Wache", "Pflege", "Kleidung herstellen", "Waffen und Rüstungen herstellen"]



aktivitaetenString = []

for aktivitaet in aktivitaeten:
    aktivitaetenString.append(str(aktivitaet) + " - " + str(aktivitaeten[0]))
choicesString = []



person = Person("Harry")
print(*Person.giveStrList(person))


print("Guten Tag, Reisender.", "Du hast die Kontrolle über ein kleines Dorf erhalten. In diesem Dorf leben bis jetzt " + str(einwohnerAnzahl) + " Einwohner.", "", "Die Einwohner tun Folgendes:", "", *aktivitaetenString)

print("Was möchtest du tun?", "", *choicesString)