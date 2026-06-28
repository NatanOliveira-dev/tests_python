def operaçoes():
    v1 = int(input("Informe os valores para as operações: "))
    v2 = int(input("Informe os valores para as operações: "))

    soma = v1 + v2
    subtracao = v1 - v2
    multiplicacao = v1 * v2

    if v2 == 0:
        divisao = None
    else:
        divisao = v1 / v2
    
    return v1, v2, divisao, soma, subtracao, multiplicacao


v1, v2, divisao, soma, subtracao, multiplicacao = operaçoes()S

print(f"A soma de {v1} + {v2} é igual a: {soma}")
print(f"A subtração de {v1} - {v2} é igual a: {subtracao}")
print(f"A multiplicação de {v1} x {v2} é igual a: {multiplicacao}")

if divisao is None:
    print("Não é possível dividir por zero")
else:
    print(f"A divisão de {v1} / {v2} é igual a: {divisao}")

