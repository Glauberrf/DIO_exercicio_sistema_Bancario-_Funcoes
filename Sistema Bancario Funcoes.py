import textwrap


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

AGENCIA = "0001"
clientes =[]
contas = []

def Menu():
    menu = """\n

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo cliente
    [5] Listar clientes
    [6] Criar nova conta
    [7] Listar contas
    [0] Sair

    => """
    return input(textwrap.dedent(menu))






def CadastroCliente(clientes):
    cpf = input("Informe o CPF do cliente (aceita-se apenas números): ")
    cliente = obter_cliente(cpf, clientes)

    if(cliente):
        print(f"O cliente {cliente} já existe para o CPF {cpf}")

    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")
    endereco = input("Informe o endereço do cliente: ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento,"cpf":cpf,"endereco":endereco})
    print(f"Cliente {nome} cadastrado com sucesso!" )

def obter_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def ListarClientes():

    for cliente in clientes:
        print(cliente)

def CriarConta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do cliente: ")
    cliente = obter_cliente(cpf, clientes)

    if(cliente):
        print(f"Conta criada com sucesso!\nDados da conta\n Nome: {cliente['nome']}\n Agencia:{agencia} - Conta: {numero_conta}")
        return {"agencia":agencia, "numero_conta": numero_conta, "cliente":cliente}
    print(f"Cliente não encontrado, por favor cadastre o cliente antes de criar a conta bancaria")

def ListarContas():
    for conta in contas:
        print(conta)

def Deposito(saldo, valor, extrato, /):
    

    if valor > 0:
        saldo = saldo + valor#+= valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")        

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

    
    

def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"O saque de R$ {valor:.2f} foi realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def Extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")        
    if(len(extrato) <= 0):
        print("Não foram realizadas movimentações.")
    else:
        for conteudo_Extrato in extrato:
            print(conteudo_Extrato)

    print(f"\nSaldo: R$ {saldo:.2f}")    
    print("==========================================")


while True:

    opcao = Menu()

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = Deposito(saldo, valor, extrato)
        
        

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = Saque(saldo = saldo, 
                             valor = valor, 
                             extrato = extrato, 
                             limite=limite, 
                             numero_saques = numero_saques, 
                             limite_saques = LIMITE_SAQUES,)
        
        

    elif opcao == "3":
       
        Extrato(saldo, extrato=extrato)

    elif opcao == "4":
       
        CadastroCliente(clientes)

    elif opcao == "5":
       
       ListarClientes()
        

    elif opcao == "6":       
       numero_conta = len(contas) + 1
       conta = CriarConta(AGENCIA, numero_conta, clientes)
       if(conta):
           contas.append(conta)
        
    elif opcao == "7":
        ListarContas()

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")





#Execicio: Glauber Roberto Fernandes