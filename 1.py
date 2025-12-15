print('============12 месяцев============')

for n in range(1,14): #ну ту надо поделить 365 на 28, тк по уравнению 28n = 365 ¯_(ツ)_/¯
    for k in range(1,13): #по такому же принципу -> 365/30
        for m in range(1,12): #тоже самое
            if 28*n+ 30*k + 31*m == 365:
                print(f'n={n}, k={k}, m={m}')
                break
            else:
                continue
            break
        else:
            continue
        break
