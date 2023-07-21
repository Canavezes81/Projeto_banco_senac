def menu():
    menu = """
    ========== M E N U ============
    [D] Depositar:
    [S] Sacar:
    [E] Extrato:
    [N] Nova Conta:
    [L] Listar Usuários:
    [U] Novo Usuário:
    [Q] Sair:

    =>
    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
    else:
        print("@@@ Operação falhou! O valor informado é inválido!")
        
        return saldo, extrato
    
def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação Falhou. Você não tem saldo suficiente!")
    
    elif excedeu_limite: 
        print("Operação Falhou. O valor do saque excede o limite.")
    
    elif excedeu_saques:
        print("Operação Falhou. Número máximo de saques excedidos.")
    
    elif valor > 0: 
        saldo -= valor
        extrato +=f"Saque: R$ {valor:.2f}"
        print("=== Saque realizado com sucesso! ===")
        numero_saque += 1
        
    else:
        print("@@@ Operação Falhou! O valor informado é inválido! @@@")
        
    return saldo, extrato

def exibir_extrato(saldo, /, *,  extrato):
    print("\n======EXTRATO=======")
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("Não foram realizadas movimentações. " if extrato == "" else extrato)
    print("\n======================================")
    
# O programa deve armazenar os usuários em uma lista. Um usuário e composto por:
# nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: longradouro, 
# nro - bairro - cidade/sigla do estado.
# Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

def novo_usuario():
    cpf = input("Informe o CPF (Somente números):")
    usuario = 0
    
    if usuario:
        print("@@@ Já exist um usuário com esse CPF @@@")

    nome = input("Informe o nome completo: ")
    data_de_nascimento =  input("Informe a data de nascimento DD-MM-AAAA: ")
    endereco = input("Informe o endereço (Longradouro, NRO - Bairro - Cidade/Sigla Estado):")
    
    print(" === Usuário cadastrado com sucesso! ====")

def nova_conta():
    cpf = input('Informe o CPF do usuário (Somente números): ')
    usuario = 0

    if usuario:
        print('==== Conta criada com sucesso ===')
        return {'Nome: ': nome, 'Data de nascimento: ': data_de_nascimento, 'Endereço: ': endereco}
    
    else:
        print("@@@ Usuário não encontrado, favor cadastrar usuário! @@@")

def listar_usuarios():
    usuarios_filtrados = [user for user in usuarios if usuarios['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = [] 
    contas = []
    
    while True:
        opcao = menu()

        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))

            depositar(saldo, valor, extrato)
        
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))

            saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
        
        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'N':
            nova_conta()

        elif opcao == 'L':
            listar_usuarios()
        
        elif opcao == 'U':
            novo_usuario()

        elif opcao == 'Q':
            print('Obrigado pela preferência!')
            break

        else:
            print('Operação inválida, favor selecionar novamente a operação desejada')
