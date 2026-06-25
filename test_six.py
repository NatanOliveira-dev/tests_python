def medias_alunos():
    medias = []
    aprovados = 0
    reprovados = 0

    for i in range(6):
        print(f"\n{i + 1}° aluno:\n")

        notas = []

        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Informe a {j + 1}° nota: "))

                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Informe um valor entre 0 e 10.")
                        
                    
                except ValueError:
                    print("Nota inválida! Informe somente números e valores entre 0 e 10.Tente novamente!")

        media = sum(notas) / len(notas)
        medias.append(media)
                    
        if media >= 6:
            aprovados += 1
        else:
            reprovados += 1

    return medias, aprovados, reprovados 

medias, aprovados, reprovados = medias_alunos()

for n in range(len(medias)):
    print(f"{n + 1} obteve a média: {medias[n]:.1f}")

print(f"Total de aprovados: {aprovados}")
print(f"Total de reprovados: {reprovados}")

