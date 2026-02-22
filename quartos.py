quartos = {
    101: "disponivel",
    102: "disponivel",
    103: "disponivel"
}

def listar_quartos():
    for numero, estado in quartos.items():
        print("Quarto", numero, "-", estado)
