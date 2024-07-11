def hub():
    hub= '''
====================
| [1] Depositar    |
| [2] Sacar        |
| [3] Extrato      |
| [4] Novo usuario | 
| [5] Listar contas|
| [6] Criar Conta  |
| [7] Sair         |
====================
'''
    return input(hub)

def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("\n\Valor inserido é inválido/")

    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\nOperação Inválida, você não possui saldo")

        elif excedeu_limite:
            print("\nOperação Inválida, você não pode sacar além do limite de R$ 500,00")

        elif excedeu_saques:
            print("\nO número máximo que você pode sacar é 3 vezes")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("\n\Valor inválido/")    

        return saldo, extrato   

def mostrar_extrato(saldo, /, *, extrato):
    print("################### Extrato ###################")
    print("Não houve transações" if not extrato else extrato)
    print(f"\nSaldo = R$ {saldo:.2f}")
    print("###############################################")

def novo_usuario(usuarios):
    cpf=input("Informe seu CPF(somente números): ")
    usuario = verificacao_usuario(cpf, usuarios)

    if usuario:
        print("Esse CPF já está Cadastrado")
        return
    
    nome= input("Informe seu nome completo: ")
    data_nasc= input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco= input("Informe seu endereço (logradouro, numero-bairro-cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nasc": data_nasc, "cpf":cpf, "endereco":endereco,})

def  verificacao_usuario(cpf, usuarios):
    usuarios_verificados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_verificados[0] if usuarios_verificados  else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = verificacao_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    
    print("Usuario não encontrado, processo encerrado")

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência = {conta['agencia']}
        C/C = {conta['numero_conta']}
        Titular = {conta['usuario']['nome']}
        '''
        print(linha)


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
    

    while True:

        opcao = hub()

        if opcao == "1":
        
            valor = float(input('''__________________ Depósito __________________
            \nInforme o valor do depósito:'''))
            print("______________________________________________")
            saldo, extrato=depositar(saldo,valor,extrato)
        



        elif opcao == "2":
            valor = float(input('''__________________ Saque __________________
                \nInforme o valor que deseja sacar:'''))
            print("______________________________________________")

            saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            limite_saques=LIMITE_SAQUES,
            numero_saques=numero_saques,
        )
        

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "6":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Valor inválido, selecione uma opção válida")        
main()
        


        

