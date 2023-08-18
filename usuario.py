class Usuario:
    def __init__(self, nome, cpf, salario, email, senha): 
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.email = email
        self.senha = senha
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
        
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    
    def Cadastro(self):
        print("--- CADASTRO ---")
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        salario = input("Digite o salario: ")
        senha = input("Cadastre uma senha: ")
        
        print("-----------------------")
        print("--- INFORMAÇÕES CADASTRADAS ---")
        print("Nome: ", nome)
        print("CPF: ", cpf)
        print("Salário: ", salario)
        print("Senha: ******")
        print("-----------------------")
        
    def Autentica(self):
        print("--- LOGIN ---")
        senha = input("Digite a senha: ")
        
        if (senha == self.senha):
            print("Usuário autenticado no sistema!")
        else:
            print("Usuário não logado!")
        
        print("-------------")
    