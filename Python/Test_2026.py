import time

a = {"nome":"miguel", "nota":"10"}

print("Calculadora de 1000 que já exite de mim")
print("")
print("AGORA MAIS UMA DE 1000 CALCULADORAS QUE EU JÁ FIZ!")

num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

ele_é_burro = "Não eu acho"

escolha = input("Escolhe de 1 a 4: ")

if num1 == "a" or num2 == str:
    print("Mano não é POSSIVEL TU É BURRO")
    print("VAI TRAVAR AGORA")
    print("daqui a 3 seg")
    time.sleep(1)
    print("")
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3... TCHAUUUUUUUU")
    time.sleep(0.9)


resultado = "nada seu broxa burro"

if escolha == '1':
    resultado = num1 - num2
elif escolha == '2':
    resultado = num1 + num2
elif escolha == '3':
    if num1 == 0 or num2 == 0:
        print("jumento sabe que n da pra dividir por zero né?")
    else:
        resultado = num1 / num2
elif escolha == '4':
    resultado = num1 = num2
else:
    print("")
    print("prikito NEM SABE BOTAR DE 1 A 4")
    ele_é_burro = "SIM"


print("")
if ele_é_burro == "SIM":
    print("BIXO BURRO DO CARAMBA")

else:
    print(f"A equação ai deu, {resultado}")

print("")
if ele_é_burro != "SIM" and resultado != "nada seu broxa burro":
    print("\033[32m Você é inteligente!")
