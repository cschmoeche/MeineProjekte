import random

print("Wieviele Runden willst du spielen:")
runden = int(input())

print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein:")
a = int(input())
if a <= 10:
    a = a
else:
    print("Ungültige Eingabe! Du sollst eine Zahl zwischen 1 und 10 eingeben du Strolch. Probiere es nochmal")
    print("Bitte eine Zahl eingeben, zwischen 1 und 10 ein")
    a = int(input())

b = random.randint(1, 10)
win_human = 0
win_pc = 0
spiel = 1

print(f"Eingabe: {a}")
print(f"Computer sagt: {b}")

while spiel < runden:
    if a == b:
        print("Der Mensch gewinnt")
        win_human += 1
        spiel = spiel + 1
        print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein:")
        a = int(input())
        if a <= 10:
            a = a
        else:
            print("Ungültige Eingabe! Du sollst eine Zahl zwischen 1 und 10 eingeben du Strolch. Probiere es nochmal")
            print("Bitte eine Zahl eingeben, zwischen 1 und 10 ein")
            a = int(input())

        b = random.randint(1, 10)
        print(f"Eingabe: {a}")
        print(f"Computer sagt: {b}")
    else:
        print("Der Computer gewinnt")
        win_pc += 1
        spiel += 1
        print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein:")
        a = int(input())
        if a <= 10:
            a = a
        else:
            print("Ungültige Eingabe! Du sollst eine Zahl zwischen 1 und 10 eingeben du Strolch. Probiere es nochmal")
            print("Bitte eine Zahl eingeben, zwischen 1 und 10 ein")
            a = int(input())
        b = random.randint(1, 10)
        print(f"Eingabe: {a}")
        print(f"Computer sagt: {b}")

else:
    if a == b:
        print("Der Mensch gewinnt")
        win_human += 1
    else:
        print("Der Computer gewinnt")
        win_pc += 1
        spiel += 1

print(f"In {spiel - 1} Spielen hat der User {win_human} Spiele und der Computer {win_pc} gewonnen.")