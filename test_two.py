while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        if numero % 2 == 0:
            print(f"O número {numero} é par!")
        else:
            print(f"O número {numero} é ímpar!")
        break
    except ValueError:
        print("Valor inválido! Por favor, digite um número inteiro.")