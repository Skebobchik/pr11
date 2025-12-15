print('==========Гипотеза Эйлера о сумме степеней==========')

flag = False
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                e5= a**5 + b**5 + c**5 + d**5
                e = int(e5 ** 0.2)
                if e**5 == e5 and e <= 150:
                    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
                    print(f'Сумма a+b+c+d+e >>> {a+b+c+d+e}')
                    flag = True
                    break
