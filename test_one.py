soma = 0

for i in range(4):
    nota = float(input(f"Informe a {i + 1}° nota: "))
    soma += nota

media = soma / 4

print(f"A média das notas é: {media:.1f}")
