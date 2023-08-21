from usuario import Usuario

class Presidente(Usuario):
    def __init__(self, nome, cpf, salario, email, senha):
        super().__init__(nome, cpf, salario, email, senha)
        
    def Cadastro(self):
        return super().Cadastro()
    
    def Autentica(self):
        return super().Autentica()