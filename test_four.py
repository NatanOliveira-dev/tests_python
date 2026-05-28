medias = []
aprovados = 0

for i in range(4):
    notas = []

    print(f"Aluno {i + 1}: ")

    for j in range(4):
    
        while True:
             try:
                nota = float(input(f"Digita a {j + 1}° nota: "))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
             except ValueError:
                print("Entrada inválida. Digite um número.")

    media = sum(notas) / len(notas)
    medias.append(media)

    if media >= 7:
            aprovados += 1


for n in range(len(medias)):
    print(f"A média do aluno {n + 1} é: {medias[n]:.1f}")
print(f"O número de alunos aprovados é: {aprovados}")