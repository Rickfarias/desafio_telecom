
def recomendar_plano(consumo):

        if consumo <= 10:
            print("Plano Essencial Fibra - 50Mbps.")
        
        elif consumo > 10 or consumo <= 20:
            print("Plano Prata Fibra - 100Mbps.")
        
        elif consumo >= 20:
            print("Plano Premium Fibra - 300Mbps.")

        else:
            print("Operação falhou! Valor informado é inválido, tente novamente.")

consumo = float(input())
plano_recomendado = recomendar_plano(consumo=consumo)
print(f"{recomendar_plano}")