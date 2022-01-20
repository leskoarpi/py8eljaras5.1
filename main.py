'''
5.1 Feladat
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O
'''
def mezot_rajzol(szel, hossz):
    for sor in range(3):
        for oszlop in range(6):
            if oszlop == hossz   and szel == sor:
                print('+ ', end='')
                szel +=10
            else:
                print('O ', end='')
        print()
        
mezot_rajzol(0,4)
