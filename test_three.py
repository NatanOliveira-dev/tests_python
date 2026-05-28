while True:
    try:
        numero = float(input("Digite um número entre 0 e 10: "))

        if 0 <= numero <= 10:
            print(f"O número {numero} é válido!")
            break
        else:
            print(f"O número {numero} é inválido!")

    except ValueError:
        print("Valor inválido. Por favor, digite um número.")