# Funcionalidade de gestão de reservas
reservas = []

def criar_reserva(cliente, quarto):
    reservas.append((cliente, quarto))
    print("Reserva criada com sucesso.")

def listar_reservas():
    for reserva in reservas:
        print("Cliente:", reserva[0], "Quarto:", reserva[1])
