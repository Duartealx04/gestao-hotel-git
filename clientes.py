clientes = []

def adicionar_cliente(nome):
    clientes.append(nome)
    print("Cliente adicionado com sucesso.")

def listar_clientes():
    print("\nLista de Clientes:")
    for cliente in clientes:
        print(cliente)
