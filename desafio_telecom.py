def menu():
    menu = """
    ========== MENU ==========
    Selecione a opção desejada

        [1]- Plano ideal
        [2]- 0

    => """
    return input(menu)

def main():
    opcao = menu

    if opcao == "1":
        consumo = float(input("Insira o seu consumo médio mensal: "))