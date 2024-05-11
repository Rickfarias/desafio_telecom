
def recomendar_plano(consumo):

        if consumo <= 10:
            print("Plano Essencial Fibra - 50Mbps.")
        
        elif consumo > 10 and consumo < 20:
            print("Plano Prata Fibra - 100Mbps.")
        
        else:
            print("Plano Premium Fibra - 300Mbps.")

consumo = float(input())
plano_recomendado = recomendar_plano(consumo=consumo)
print(recomendar_plano(consumo))