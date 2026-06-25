def ages():
    idades = []
    maior_idade = 0

    for i in range(8):
        while True:
            try:
                idade = int(input(f"{i + 1}º Pessoa. \nInforme sua idade: ")) 

                if 0 <= idade <= 120: # Verifica as idades determinadas.
                    idades.append(idade)

                    if idade >= 18:
                        maior_idade += 1
                    break
                else:
                    print("Idade inválida! Informe uma idade entre 0 e 120.")

            except ValueError:
                print("Idade inválida! Informe uma idade entre 0 e 120.")
           
    media_idades = sum(idades) / len(idades)

    return idades, media_idades, maior_idade 


idades, media_idades, maior_idade = ages()

for n in range(8):
    print(f"A {n + 1}ª Pessoa tem {idades[n]} anos de idade!\n")
    
print(f"Maior idade informada: {max(idades)}\n")
print(f"Menor idade informada: {min(idades)}\n")
print(f"Média das idades informadas: {media_idades:.2f}\n")
print(f"Quantidade de maiores de idade informados: {maior_idade}")



