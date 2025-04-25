import winshell

def limpar_lixeira():
    print("Limpando a lixeira...")
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
    print("Lixeira limpa com sucesso!")

if __name__ == "__main__":
    limpar_lixeira()
