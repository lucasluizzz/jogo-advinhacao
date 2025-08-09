import random

numeroaleatorio = random.randint(1,100)
# print(f"[DEBUG] Número sorteado: {numeroaleatorio}")  # REMOVA DEPOIS

escolha = int(input("Escolha um número de 1 a 100: "))

while escolha != numeroaleatorio:
    if escolha > numeroaleatorio:
        print("O número escolhido é maior que o número a adivinhar.")
    else:
        print("O número escolhido é menor que o número a adivinhar.")
    
    escolha = int(input("Escolha outro número: "))

print("Parabéns, você acertou o número!")
