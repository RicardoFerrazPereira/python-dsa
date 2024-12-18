# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

# Como eu fiz de começo

# print("\n******************* Calculadora em Python *******************")

# print('\nSelecione o número da operação desejada:')

# print('\n1 - Soma')
# print('2 - Subtracao')
# print('3 - Multiplicacao')
# print('4 - Divisao')

# operacao = int(input("Digite sua opcao (1/2/3/4): "))
# print(operacao)

# num1 = int(input("\nDigite o primeiro numero: "))
# num2 = int(input("\nDigite o segundo numero: "))

# if(operacao ==  1):
#     t = num1 + num2
# elif(operacao == 2):
#     t = num1 - num2
# elif(operacao == 3):
#     t = num1 * num2
# elif(operacao == 4):
#     t = num1 / num2
# else:
#     "Erro"

# print(t)

def calculadora():

    print("\n******************* Calculadora em Python *******************")

    print("\nSelecione a operação desejada:")
    print("1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao")

    try:
        # Receber a operação
        operacao = int(input("\nDigite sua opção (1/2/3/4): "))

        # Validar operação
        if operacao not in [1, 2, 3, 4]:
            print("Erro: Operação inválida. Por favor, escolha entre 1 e 4.")
            return    

        # Receber os números
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("\nDigite o segundo número: "))    

        # Dicionário de operações
        operacoes = {
            1: ('Soma', lambda x, y: x + y),
            2: ('Subtração', lambda x, y: x - y),
            3: ('Multiplicação', lambda x, y: x * y),
            4: ('Divisão', lambda x, y: x / y if y != 0 else "Erro: Divisão por zero")
        }  

        # Executar operação
        nome_op, funcao = operacoes[operacao]
        resultado = funcao(num1, num2)    

        print(f"\n{nome_op} de {num1} e {num2} = {resultado}")      

    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")                                        

# Executar a calculadora
calculadora()
