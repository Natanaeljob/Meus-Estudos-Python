plv = str( input('Digite sua expressão: ')).strip()
pa = list()
co = list()
ch = list()

for t in plv:
    if t == '(':
        pa.append(t)
    elif t == ')':
        if len(pa) > 0:
            pa.pop()
        else:
            pa.append(t)
            break

    if t == '[':
        co.append(t)
    elif t == ']':
        if len(co) > 0:
            co.pop()
        else:
            co.append(t)
            break
    
    if t == '{':
        ch.append(t)
    elif t == '}':
        if len(ch) > 0:
            ch.pop()
        else:
            ch.append(t)
            break


if len(pa) == 0 and len(co) == 0 and len(ch) == 0:
    x = '\033[32mCORRETA\033[m'
else:
    x = '\033[31mINCORRETA\033[m'

print(f'Sua operação está {x} !!!')