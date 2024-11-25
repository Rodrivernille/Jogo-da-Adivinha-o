import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (número entre 1 e 50)")
    print("2 - Médio (número entre 1 e 100)")
    print("3 - Difícil (número entre 1 e 200)")
    
    # Escolha do nível de dificuldade
    while True:
        try:
            nivel = int(input("Digite o número do nível desejado: "))
            if nivel == 1:
                limite = 50
                tentativas_max = 10
                break
            elif nivel == 2:
                limite = 100
                tentativas_max = 7
                break
            elif nivel == 3:
                limite = 200
                tentativas_max = 5
                break
            else:
                print("Escolha um nível válido (1, 2 ou 3).")
        except ValueError:
            print("Por favor, insira um número válido.")

    # Gera o número aleatório
    numero_secreto = random.randint(1, limite)
    tentativas = 0

    print(f"\nTente adivinhar o número entre 1 e {limite}. Você tem {tentativas_max} tentativas!")

    while tentativas < tentativas_max:
        try:
            chute = int(input("Digite o seu palpite: "))
            tentativas += 1

            # Verifica o palpite
            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
                break
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Exibe tentativas restantes
        print(f"Tentativas restantes: {tentativas_max - tentativas}")
    
    # Caso o jogador não acerte
    if tentativas == tentativas_max and chute != numero_secreto:
        print(f"😢 Você perdeu! O número era {numero_secreto}. Tente novamente!")

# Inicia o jogo
jogo_adivinhacao()
