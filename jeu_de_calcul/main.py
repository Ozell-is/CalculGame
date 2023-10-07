import random

#ajouter exception div by 0 et modulo by 0

sign = ['+', '-', '*', '/','%']
sign = random.choice(sign)
restart = 'yes'






while restart == 'yes':

    a = random.randint(-10,10)
    b = random.randint(-10,10)

    response = input(f'Combien font {a} {sign} {b}' '\n')
    calcul = eval(str(a) + sign + str(b))

    if response == str(calcul):
        print('bonne réponse!')
        while restart != '1' or restart != '2':
            restart = input('veux-tu rejouer?'"\n"
                            '1 pour oui'"\n"
                            '2 pour non' "\n")
            if restart == '1':
                restart = 'yes'
            else:
                print('bonne soirée')


    else:
        print(f't\'est naze, la réponse était {calcul}' )
        while restart != '1' or restart != '2':
            restart = input('veux-tu rejouer?'"\n"
                        '1 pour oui'"\n"
                        '2 pour non' "\n")
            if restart == '1':
                restart = 'yes'
            else:
                print('bonne soirée')
            break


if restart == 'non':
    print('bonne soirée')