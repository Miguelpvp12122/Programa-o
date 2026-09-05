

Saldo = 0
Nome = ""
Senha = ""
Tot = 0

nome = str(input("Digite nome de usuario: "))
Nome = nome
while True:
    senha = str(input("Digite sua senha: "))
    if len(senha) >= 8:
        print("Senha criada.")
        Senha = senha
        break
    else:
        print("Escreva uma senha que tenha 8 caracteres.\n")


print("Lista de comandos:\n1. Ver conta\n2. Depositar dinheiro\n3. Retirar dinheiro\n")


Res = str(input("Oque deseja fazer?"))

if Res == "1":
    if Nome == "":
        print("Ainda não contem usuario.")
    else:
        print(f"Nome: {Nome}")
        print(f"Saldo: {Saldo}")
        carac = len(Senha)
        print(f"Senha: {"*"*carac}")
            
        
if Res == "2":
    if Nome == "":
        print("Ainda não contem usuario.")
    else:
        dinheiro = int(input("Quanto deseja depositar: "))
        while True:
            dig_senha = str(input("Digite sua senha: "))
            Tot += 1
            if dig_senha == Senha:
                Tot = 0
                Saldo += dinheiro
                break
            elif Tot == 3:
                print("Limite atingido")
                Tot = 0
                break
            else:
                print("Senha errada, digite novamente")

if Res == "3":
    if Nome == "":
        print("Ainda não contem usuario.")
    else:
        dinheiro = int(input("Quanto deseja retirar: "))
        if dinheiro > Saldo:
            print("Não contém dinheiro o suficiente")
        else:
            while True:
                dig_senha = str(input("Digite sua senha: "))
                if dig_senha == Senha:
                    Saldo -= dinheiro
                    break
                else:
                    print("Senha errada, digite novamente")

