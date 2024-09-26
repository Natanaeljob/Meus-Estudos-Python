def leiaint(x):
    while True:
        n = str( input(x)).strip()
        print('')
        if n.isnumeric():
            n = float(n)
            if n.is_integer:
                n = int(n)
                break
        else:
            print( '\033[31m!!Erro!! Digite um número inteiro valido!\033[m')
            print('')
    return f'\033[32m{n}\033[m'


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
