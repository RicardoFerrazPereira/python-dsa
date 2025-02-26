# Projeto 1 - Desenvolvimento de Game emLinguagem Python - V1

# Import 
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    #Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    limpa_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'melancia', 'manga', 'kiwi', 'melão', 'caju', 'acerola', 'carambola', 'cereja', 'framboesa', 'goiaba', 'graviola', 'jabuticaba', 'jaca', 'limão', 'lima', 'maçã', 'mamão', 'mangaba', 'maracujá', 'melão', 'pêssego', 'pomelo', 'tangerina', 'tamarindo', 'tomate', 'abacaxi', 'amora', 'cereja', 'figo', 'framboesa', 'goiaba', 'graviola', 'jabuticaba', 'jaca', 'limão', 'lima', 'maçã', 'mamão', 'mangaba', 'maracujá', 'melão', 'pêssego', 'pomelo', 'tangerina', 'tamarindo', 'tomate', 'abacaxi', 'amora', 'cereja', 'figo', 'framboesa', 'goiaba', 'graviola', 'jabuticaba', 'jaca', 'limão', 'lima', 'maçã', 'mamão', 'mangaba', 'maracujá', 'melão', 'pêssego', 'pomelo', 'tangerina', 'tamarindo', 'tomate']
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    while chances > 0:

        # Imprime o texto da forca
        print(" ".join(letras_descobertas)) # join - faz uma junção de strings do que está no lado esquerdo com o lado direito
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower() # lower - converte todas as letras para minúsculas

        # Condicional - Checando cada tentativa
        if tentativa in palavra:
            index = 0 

            # Para cada letra dentro da palavra, vou verificar se a tentativa é igual a letra
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa) # append só pode ser usado em lista

        # Condicional
        # Se o _ não estiver na lista de letras descobertas, o usuário venceu
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    
        
    # Condicional
    # Se o _ estiver na lista de letras descobertas, o usuário perdeu
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

# Bloco main -> dizer ao interpretador que isso é um código python
if __name__ == "__main__":
    game()
    print("\nParabéns")