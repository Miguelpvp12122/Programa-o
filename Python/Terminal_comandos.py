print("\033[35m-----Iniciando Ajuda-----\033[m \n")

print("\033[36m=====Comandos:=====")
print("- Comandos = :Commands\033[m \n")


while True:
    Res = str(input("$: "))
    if Res == ":Commands" or Res == ":commands":
        break
    else:
        print(f'\n\033[31mO comando "{Res}" não foi encontrado\033[m\n')

print('\nCriar arquivo              = "type nul > (Nome do arquivo)"')
print('Criar pasta              = "mkdir (Nome da pasta)"')
print('Ver pasta                = "dir"')
print('Ver pasta limpa          = "dir /b"')
print('Entar em pasta           = "cd (Nome da pasta)"')
print('Voltar pasta             = "cd .."')
print('Apagar arquivo           = "del (Nome do arquivo)"')
print('Limpar terminal          = "cls"')
print('Ver conteudo do arquivo  = "type"')
print('Mover arquivo/pasta      = "move"')
print('Trocar nome A/P          = "ren"')

print('Iniciar repositorio      = "git init"')
print('Status do repositorio    = "git status"')

print('Adicionar ao stage       = "git add (Nome do arquivo)"')
print('Adicionar tudo ao stage  = "git add ."')
print('Remover do estado stage  = "git rm --cached (Nome do arquivo)"')
print('Remover todos do stage   = "git reset"')
print('Fazer commit             = "git commit -m "(Mensagem)"')
print('Fazer commit (Outra P)   = "git commit -m "(Mensagem)" "--author=(Nome da pessoa) <(Email)>"')
print('Lista de commit          = "git log"')
print('Lista de commit (menor)  = "git log --oneline"')

print('Voltar pra um commit     = "git checkoud (Id do commit)"')
print('Voltar pra o (Head)      = "git checkoud master"')
print('Revertendo commit        = "git revert (id do commit)"')
print('Resetando totalmente     = "git reset (id do commit) --hard"')

print('Ver branch"s             = "git branch"')
print('Fazer branch             = "git branch (Nome do novo branch)"')
print('Renomear branch          = "git branch -m (Nome do branch) (novo nome)"')
print('Apagar branch            = "git branch -D (Nome do branch)"')
print('Fundir branch            = "git merge (Nome do branch)"')

print('Mandar pro Github        = "git push (Nome do repositorio do github) (Branch que deseja)"')
print('Pegar rep do github      = "git clone (Nome do repositorio do github)"')
print('Puxar do Github          = "git pull (Nome do repositorio do github) (Branch que deseja)"')
print('clonar rep do Github     = "git clone (Nome do repositorio do github) (Nome que deseja)"')

print('Adicionar "Apelido"      = "git remote add (Nome desejado) (Nome do repositorio do github)"')
print('Ver apelido "Apelido"    = "git remote -v"')

print('Ignorar arquivos         = "(Nome do arquivo).gitignore"')
