saldo = 0.0
LIMITE_SAQUES = 5
num_saques = 0
extrato = ""
usuarios = []
AGENCIA_NUMERO = 0001
NUMERO_CONTA = 0
contas = []

def gerar_numero_conta():
    global NUMERO_CONTA
    NUMERO_CONTA += 1
    return NUMERO_CONTA

def criar_conta (lista_contas, lista_usuarios):
    cpf_caracteres = input("Informe seu CPF (somente números): ")
    cpf_limpo = "".join(filter(str.isdigit, cpf_caracteres))

    usuario = filtrar_usuarios(cpf_limpo, lista_usuarios)

    if not usuario:
        print("ERRO! Não existe nenhum usuário cadastrado com esse CPF")

    numero_conta = gerar_numero_conta()
    conta = {
        "agencia": AGENCIA_NUMERO,
        "numconta": numero_conta,
        "usuario": usuario
    }

    lista_contas.append(conta)

def cadastrar_usuarios(lista_usuarios):
    cpf_caracteres = input("Informe seu CPF (somente números): ")
    cpf_limpo = "".join(filter(str.isdigit, cpf_caracteres))

    if filtrar_usuarios(cpf_limpo, usuarios):
        print("\n Erro, este CPF já está cadastrado!")

    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa)")
    
    logradouro = input("Informe seu logradouro (Rua, Av, etc.): ")
    bairro = input ("Informe seu bairro: ")
    cidade = input("Informe sua cidade: ")
    sigla_estado = input("Informe a sigla do estado: ")
    endereco = f"{logradouro}, {bairro}, {cidade}-{sigla_estado}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_limpo,
        "endereco": endereco
    }

    lista_usuarios.append(usuario)
    print ("\n === Usuário Cadastrado com sucesso! ===")

def filtrar_usuarios(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf" == cpf]]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def saque (valor_saque, limite_diario_saques, limite_valor_saque = 500):
    if valor_saque <= 0:
        print("Você não pode sacar valores negativos ou igual a 0")
    global saldo
    global extrato
    global num_saques

    excedeu_limite_diarios = num_saques >= limite_diario_saques
    excedeu_limite = valor_saque > limite_valor_saque
    excedeu_saldo = valor_saque > saldo

    if excedeu_limite_diarios:
        print("Você excedeu o limite de saque diarios!")
    elif excedeu_limite:
        print(f"Valor máximo de saque é R${limite_valor_saque}")
    elif excedeu_saldo:
        print(f"Saldo Insuficiente!")
    else:
        saldo -= valor_saque
        print(f"Saque de R${valor_saque} realizado com sucesso!")
        num_saques+= 1
        extrato += f"\nSaque: R${valor_saque}"

def depositar(valor_deposito):
    global saldo
    global extrato

    if valor_deposito <= 0:
        print("Você não pode realizar depósitos de valores negativos ou igual a 0!")
    else:
        saldo += valor_deposito
        print(f"Depósito de R${valor_deposito} realizado com sucesso!")
        extrato += f"\nDepósito: R${valor_deposito}"

def ver_extrato():
    print("===== EXTRATO =====")
    print("Não foi realizado movimentações" if not extrato else extrato)
    print(f"Saldo Atual: {saldo}\n Extrato: {extrato}")


