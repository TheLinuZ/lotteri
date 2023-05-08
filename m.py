import lotteri
import os

lotteriet = lotteri.Lotteri()
looping = True

while looping:

    os.system('cls' if os.name == 'nt' else 'clear')
    antal_lotter = input("\n\tHur många lotter vill du ha? (Max 3 lotter): ")

    try:
        int_antal_lotter = int(antal_lotter)
        i = 0

        if(int_antal_lotter < 4):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\tGrattis du vann: ")

            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print(vinst)
                i += 1


        elif(int_antal_lotter > 3):
            print("\n\tDu har valt för många lotter! ")

    except ValueError:
        print("Endast siffror tillåtna")

    print("----------------------------------------------------------------------------")
    spela_igen = input("\n\t\tVill du spela igen? J/N -> ")

    if(spela_igen == "n"):
        break

#print(lotteriet.get_vinst())