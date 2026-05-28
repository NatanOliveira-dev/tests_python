while True:
    try:
        valor = int(input("Digite um número inteiro: "))
        
        if valor % 2 == 0:
            print(f"O número {valor} é par!")
        else:
            print(f"O número {valor} é ímpar!")
        break

    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")
        