print('=======Старинная задача======')

for bulls in range(1, 11): #а тута 100 на 10
    for cows in range(1, 21): #тут нада 100 на 5 поделить, получится 20 = макс. кол. коровок муууууу
        for calves in range(1, 201): #100/0.5
            if bulls*10 + cows*5 + calves*0.5 == 100:
                print(f'Быков >>> {bulls}, Коровок >>> {cows}, Телят >>> {calves}')
