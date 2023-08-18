from usuario import Usuario
from funcionario import Funcionario
from gerente import Gerente
from diretor import Diretor
from secretario import Secretario
from presidente import Presidente
from conta_bancaria import Conta


def main():
    print("--------------------")
    print("----- CITIBANK -----")
    print("--------------------")
    print("OLÁ! SEJA BEM VINDO (A) ")

    
    tipo_conta = input("Informe o tipo de conta (usuario, funcionario, gerente, diretor, secretario, presidente): ")
    if tipo_conta == "usuario":
        usuario = Usuario('Fernanda', '000.000.000-00', 1500.00, 'fernanda@email.com', '123')
        usuario.Autentica()
        print("ESCOLHA O SERVIÇO: ")
        print("[1] DADOS CONTA")
        print("[2] EXTRATO")
        print("[3] SAQUE")
        print("[4] PIX")
        print("[5] SALDO")
        print("[6] PAGAMENTO")
        print("[7] EMPRÉSTIMO")
        print("[8] DEPÓSITO")
        
        opcao = int(input("Digite uma opção: "))
        c1 = Conta('Fernanda', '000.000.000-00', 1500.00, 'fernanda@email.com', '123', '123-4', '10856-0', 300.00, 100)
        
        if (opcao == 1):
            return c1.Dados_Conta()
        elif (opcao == 2):
            return c1.Extrato_Conta()
        elif (opcao == 3): 
            return c1.Saque_Conta()
        elif (opcao == 4):
            return c1.Pix_Conta()
        elif (opcao == 5):
            return c1.Saldo_Conta()
        elif (opcao == 6):
            return c1.Pagamento_Conta()
        elif (opcao == 7):
            return c1.Emprestimo_Conta()
        elif (opcao == 8):
            return c1.Depositar_Conta()
        else:
            print("Opção inválida!")
    
    elif tipo_conta == "funcionario":
        funcionario = Funcionario('Maria', '111.111.111-11', 2500.00, 'funcionario@email.com', '123456')
        funcionario.Autentica()
        
    elif tipo_conta == "gerente":
        gerente = Gerente('José', '222.222.222-22', 3500.00, 'gerente@email.com', '123456789', 10)
        gerente.Autentica()
        
    elif tipo_conta == "diretor":
        diretor = Diretor('Marcos', '333.333.333-33', 4500.00, 'diretor@email.com', '1234')
        diretor.Autentica()
        
    elif tipo_conta == "secretario":
        secretario = Secretario('Josefa', '444.444.444-44', 2000.00,'secretario@email.com', '12345')
        secretario.Autentica()
        
    elif tipo_conta == "presidente":
        presidente = Presidente('Paulo', '555.555.555-55', 10000.00, 'presidente@email.com', '1234567')
        presidente.Autentica()
    else:
        print("Tipo de conta inválido.")    
    print("--------------------")

if __name__ == "__main__":
    
    main()

