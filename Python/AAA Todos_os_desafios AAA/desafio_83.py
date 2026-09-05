espressão = str(input('digite uma explessão: '))
listra = []

for sim in espressão:
    if sim == '(':
        listra.append('(')
    elif sim == ')':
        if len(listra) > 0:
            listra.pop()
        else:
            listra.append(')')
            break

if listra == 0:
    print('ela está certa')
else:
    print('ela está errada')