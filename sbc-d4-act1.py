from random import choice

# Player input and assignment
p1 = input("Kulob or hayang >").capitalize()
print(f"P1 = {p1}")

# Random choices for the computer
com1 = choice(["Kulob", "hayang"])
com2 = choice(["Kulob", "hayang"])
print(f"C2 = {com1}\nC3 = {com2}")

# Determine the winner
if p1 == com1 == com2:
    print("It's a tie!")
elif (p1 == "Kulob" and com1 == "hayang" and com2 == "hayang") or (p1 == "hayang" and com1 == "Kulob" and com2 == "Kulob"):
    print("P1 Wins!!!!")
elif (com1 == "Kulob" and p1 == "hayang" and com2 == "hayang") or (com1 == "hayang" and p1 == "Kulob" and com2 == "Kulob"):
    print("C2 Wins!!!!")
else:
    print("C3 Wins!!!!")