from random import randint

choice0 = "Fold"
choice1 = "Unfold"
ran = randint(0,1)
dan = randint(0,1)

user = input("Choose Fold or Unfold >")
if user.capitalize() == "Fold":
    p1 = "Fold"
    print("P1 = ", user)
else:
    p1 = "Unfold"
    print("P1 = Unfold")

com1 = ran
if com1 == 1:
    com1 = "Fold"
    print("C1 = Fold")
else:
    com1 = "Unfold"
    print("C1 = Unfold")

com2 = dan
if com2 == 1:
    com2 = "Fold"
    print("C2 = Fold")
else:
    com2 = "Unfold"
    print("C2 = Unfold")


if (p1 == "Fold" and com1 == "Unfold" and com2 == "Unfold") or (p1 == "Unfold" and com1 == "Fold" and com2 == "Fold"):
    print("P1 Win!")


elif (p1 == "Unfold" and com1 == "Fold" and com2 == "Unfold") or (p1 == "Fold" and com1 == "Unfold" and com2 == "Fold"):
    print("C1 Win!")


elif (p1 == "Unfold" and com1 == "Unfold" and com2 == "Fold") or (p1 == "Fold" and com1 == "Fold" and com2 == "Unfold"):
    print("C2 Win!")


else:
    print("No one wins!")