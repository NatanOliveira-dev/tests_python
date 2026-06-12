def pedir_notas(quantidade):
    notas = []


    for i in range (quantidade):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas.append(nota)


    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

notas_bimestrais = pedir_notas(4)
media = calcular_media(notas_bimestrais)

print(f"A média das notas é: {media:.1f}")