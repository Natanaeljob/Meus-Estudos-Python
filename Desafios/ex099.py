from time import sleep

def maior(*obs):
    l = len(obs)
    for gg in obs:
        print(gg, end = ' ', flush = True)
        sleep(1)
    print('')
    print(f'Tem {l} números na lista.')
    x = max(obs)
    print(f'O maior deles é {x}')
    print('_'*36)
    print('')

print('_'*36)
print('')

print('Lista 1:\n')
maior(1,2,3)

print('Lista 2: \n')
maior(9,5,1,7)