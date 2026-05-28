media = []

for i in range(4):

    nota = float(input(f"Digita a a {i + 1}ª nota: "))
    media.append(nota)

    medias = sum(media) / len(media)

print(f"A média do aluno é: {medias:.1f}")
