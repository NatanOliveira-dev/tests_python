def dados():
    nome = (input("Informe o seu nome: "))
    idade = int(input("Informe sua idade: "))
    curso = (input("Informe seu curso: "))

    return nome, idade, curso


nome, idade, curso = dados()

print(f"{nome} tem {idade} anos e cursa {curso}!")S