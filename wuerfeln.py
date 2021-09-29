import random
a = random.randint(1, 6)
while a<6:
    print(f"Du hast eine {a} gewürfelt. Würfel nochmal")
    a = random.randint(1, 6)
else:
    print(f"Prima du hast eine {a} gewürfelt. Du darfst jetzt gehen und Bier trinken")




