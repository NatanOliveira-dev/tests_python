def impar_ou_par():
    number = int(input("Informe um valor: "))

    if number % 2 == 0:
        print(f"O número {number} é um número par!")
    else:
        print(f"O número {number} é um número ímpar!")


impar_ou_par()