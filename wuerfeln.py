import random
a = random.randint(1, 6)
runden = 0
while a<6:
    print(f"Du hast eine {a} gewürfelt. Würfel nochmal")
    a = random.randint(1, 6)
    runden += 1
else:
    print(f"Du hast eine {a} gewürfelt.")
    runden += 1
    print(f"Prima du hast eine {a} gewürfelt und dafür {runden} Versuche gebrauchst. Du darfst jetzt gehen und Bier trinken")




