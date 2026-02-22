from clientes import adicionar_cliente, listar_clientes
from quartos import listar_quartos
from reservas import criar_reserva, listar_reservas

while True:

    print("\n--- HOTEL ---")
    print("1 - Adicionar cliente")
    print("2 - Listar clientes")
    print("3 - Listar quartos")
    print("4 - Criar reserva")
    print("5 - Listar reservas")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        adicionar_cliente(nome)

    elif op == "2":
        listar_clientes()

    elif op == "3":
        listar_quartos()

    elif op == "4":
        cliente = input("Cliente: ")
        quarto = input("Quarto: ")
        criar_reserva(cliente, quarto)

    elif op == "5":
        listar_reservas()

    elif op == "0":
        break
