from usuario import Usuario


class Secretario(Usuario):
    def __init__(self, nome, cpf, salario, email, senha):
        super().__init__(nome, cpf, salario, email, senha)