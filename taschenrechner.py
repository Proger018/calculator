def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def multiplizieren(x, y):
    return x * y

def dividieren(x, y):
    if y == 0:
        return "Fehler: Division durch Null ist nicht erlaubt!"
    return x / y

print("Wähle eine Operation:")
print("1. Addieren")
print("2. Subtrahieren")
print("3. Multiplizieren")
print("4. Dividieren")


while True:
    wahl = input("Gib die Nummer der Operation ein (1/2/3/4): ")
    if wahl in ('1', '2', '3', '4'):
        break
    else:
        print("Ungültige Eingabe! Bitte wähle nur 1, 2, 3 oder 4.")

while True:
    try:
        zahl1 = float(input("Gib die erste Zahl ein (z. B. 4.5 oder 10): "))
        break
    except ValueError:
        print("Ungültige Eingabe! Bitte nur gültige Zahlen eingeben (z. B. 4.5).")

while True:
    try:
        zahl2 = float(input("Gib die zweite Zahl ein (z. B. 3 oder 2.5): "))
        break
    except ValueError:
        print("Ungültige Eingabe! Bitte nur gültige Zahlen eingeben (z. B. 3).")

if wahl == '1':
    print("Ergebnis:", addieren(zahl1, zahl2))
elif wahl == '2':
    print("Ergebnis:", subtrahieren(zahl1, zahl2))
elif wahl == '3':
    print("Ergebnis:", multiplizieren(zahl1, zahl2))
elif wahl == '4':
    print("Ergebnis:", dividieren(zahl1, zahl2))