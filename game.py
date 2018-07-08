from customprint import print as blockprint


_balance = 100
_time = 1
_units = []
_playerName = ""
_villageName = ""


class Unit:
    _name = "EINHEIT"
    _amountOwned = 0
    _increaseFactor = 0.1
    _income = 1

    def calcPriceFactor(self):
        return 1 + (self._amountOwned * self._increaseFactor)

    def currentPrice(self):
        return self.calcPriceFactor() * self._basePrice

    def getEarnings(self):
        return self._amountOwned * self._income

    def buyUnit(self):
        global _balance
        price = self.currentPrice()
        if _balance >= price:
            _balance -= price
            self._amountOwned += 1
            print("Einheit " + self.getName() + " gekauft für " + str(price) + ". Nun in Besitz: " + str(
                self._amountOwned))
            nextTurn()
        else:
            print("Zu wenig Geld")

    def getName(self):
        return self._name

    def __str__(self):
        return self._name + " - Basispreis " + str(self._basePrice) + ", Preisanstieg " \
               + str(self._increaseFactor * 100) + "% - In Besitz " + str(self._amountOwned) + ", Aktueller Preis " \
               + str(self.currentPrice())


class Farmer(Unit):
    _basePrice = 10
    _name = "Bauer"
    _increaseFactor = 0.2


class Soldier(Unit):
    _basePrice = 20
    _name = "Soldat"
    _income = 3


def nextTurn():
    global _time, _balance
    for unit in _units:
        earned = unit.getEarnings()
        print("Einheit " + unit.getName() + " in Besitz: " + str(unit._amountOwned) + " - Einkommen: " + str(earned))
        _balance += earned

    _time += 1
    reportGamestate()


def requestChoice(text, choices):
    blockprint(text)

    for x in range(len(choices)):
        print(str(x) + ". " + choices[x])

    answered = False
    while not answered:
        answer = input()
        for x in range(len(choices)):
            if answer == str(x):
                return int(answer)
        print("Bitte gib nur die Ziffer deiner Auswahl an.")


def requestText(text):
    blockprint(text + " Bitte gib deine Antwort ein.")
    while True:
        antwort = input()
        if antwort == None or antwort == "":
            print("Bitte gib etwas Sinnvolles ein.")
        else:
            break
    return antwort


# def blockprint(text):
#    print("-" * (len(text) + 4))
#    print("| " + text + " |")
#    print("-" * (len(text) + 4))


def reportGamestate():
    global _balance, _units, _time, _playerName, _villageName

    income = 0
    for unit in _units:
        income += unit.getEarnings()

    blockprint("Dorf '" + _villageName + "' von " + _playerName + ", Runde " + str(_time) + ", Einkommen " + str(
        income) + ", Gold " + str(_balance))


# initialize game

_units.append(Farmer())
_units.append(Soldier())

# introduction
blockprint("Balresch's strategy thingy")
print("Du wirst gleich die Verantwortung über ein Dorf erhalten. Hilf den Bewohnern zu überleben!")
_playerName = requestText("Wie heißt du?")
_villageName = requestText("Wie heißt dein Dorf?")
blockprint(_playerName + " erhält die Kontrolle über das Dorf " + _villageName + ".")

# First overview and first round

reportGamestate()

# Request loop

_gameactive = True
while _gameactive:

    # Display unit details
    unitlist = ["Folgende Einheiten stehen zum Kauf zur Verfügung:", ""]
    for unit in _units:
        unitlist.append(str(unit))
    unitlist.append("")
    blockprint("", unitlist, "")

    # prepare choices available this round
    choices = []

    for unit in _units:
        choices.append(unit.getName() + " kaufen")

    choices.append("Aussetzen")
    choices.append("Spiel beenden")

    # request choice formthis round from player
    action = requestChoice("Was möchtest du diese Runde unternehmen?", choices)

    for x in range(len(_units)):
        if action == x:
            _units[x].buyUnit()
    if x + 1 == action:
        nextTurn()
    elif x + 2 == action:
        _gameactive = False



