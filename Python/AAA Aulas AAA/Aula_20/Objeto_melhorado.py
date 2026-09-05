class Nova_pessoa:
    # Documentação
    """
    - A classe "Nova_pessoa" faz com que crie uma pessoa nova

    - Como fazer:
        * Variavel = Nova_pessoa

    - Funções:
        - aniversario()
            * A pessoa vai completar ano
        - mudando_nome()
            * A pessoa tem liberdade de mudar o nome
    
    !!! Se tirar print() do objeto, ira mostra uma mensagem !!!

    """

    # Metodo contrutor
    def __init__(self, nome = "Sem usuario", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        
    def mudando_nome(self):
        self.nome = str(input("Novo nome: "))

    def __str__(self):
        return f"Seu nome é {self.nome} e sua idade é {self.idade}"
    def __getstate__(self):
        return f"Nome = {self.nome} ; Idade = {self.idade}"


G1 = Nova_pessoa("Miguel", 14)
G1.aniversario()
print(G1)

#print(G1.__dict__)  * Atributo
#print(G1.__getstate__())  * Metodo
#print(G1.__doc__)  * Documentario
