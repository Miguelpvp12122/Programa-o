peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))
imc = peso/altura

if imc <=18.0:
    print('seu IMC está abaixo do peso. ')
elif imc >18.0 and imc <25.0:
    print('IMC ideal. ')
elif imc >25.5 and imc <29.9:
    print('seu IMC está na categoria sobrepeso. ')
elif imc >30.5 and imc <39.9:
    print('você está na obesidade. ')
elif imc >40:
    print('você está na obesidade mórbida. Tenha cuidado')

print({imc})