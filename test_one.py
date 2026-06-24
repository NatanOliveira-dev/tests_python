def media_alunos():
    soma = 0

    for i in range(4):
        while True:
            try:
                notas = float(input(f"Digite a {i + 1}° nota: "))

                if notas < 0 or notas > 10:
                    print("Nota inválida. Digite uma nota entre 0 e 10!")
                else:
                    soma += notas
                    break
            except ValueError:
                print("Entrada inválida. Digite um número válido!")

    media = soma / 4
    return media

resultado = media_alunos()

print(f"A média das notas dos alunos é: {resultado:.1f}")