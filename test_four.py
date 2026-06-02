medias = []
aprovados = 0

for i in range(4):
    notas = []

    print(f"\nAluno {i + 1}: \n")

    for j in range(4):
        nota = float(input(f"Informe a {j + 1}ª nota:"))
        notas.append(nota)

    media = sum(notas) / len(notas)
    medias.append(media)

    if media >= 7:
        aprovados += 1 

for i in range(4):
    print(f"\nAluno {i + 1}: \n")
    print(f"Média: {medias[i]:.1f}")
    
print(f"Total de alunos aprovados: {aprovados}")