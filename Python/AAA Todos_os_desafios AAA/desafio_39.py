data = int(input('que ano você nasceu? '))
data -= 2006
data += 18

if data <18:
    print('ainda você nao esta na idade de se alistar pro exercito. ')
elif data == 18:
    print('você esta na hora de se alistar pro exercito. ')
elif data >18:
    print('você passou da hora de se alistar va agora! ')

print({data})