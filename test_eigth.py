def produtos_vendas():
    produtos = []
    preco = []
    quantidade = []
    acima_de_100 = 0
    
    for i in range(5):
        while True:
            try:
                nomes = str(input("Informe o nome do produto: ")) 
                valor = float(input("Informe o preço do produto: "))   
                estoque = int(input("Informe a quantidade atual em estoque: "))

                if valor >= 0 and estoque >= 0:
                    produtos.append(nomes)
                    preco.append(valor)
                    quantidade.append(estoque)
                    
                    if valor >= 100:
                        acima_de_100 += 1
                    break 
                    
                else:
                    print("Valor inválido! Informe o preço positivo!")
                
            except ValueError:
               print("Valores informados inválidos. Tente novamente!")    

    return produtos, preco, quantidade, acima_de_100


produtos, preco, quantidade, acima_de_100 = produtos_vendas()

total_geral = 0

for j in range(5):
    total_produto = preco[j] * quantidade[j]
    total_geral += total_produto

    print(f"Produto cadastrado: {produtos[j]}")
    print(f"Total de produto x estoque: R$ {total_produto:.2f}")
    
print(f"Produto mais caro custa: {max(preco)}")
print(f"Produto mais barato custa: {min(preco)}")
print(f"Valor total geral no estoque: R$ {total_geral:.2f}")
print(f"Quantidade de produtos em estoque: {quantidade}")
print(f"Quantidade de produtos acima de R$ 100,00: {acima_de_100}")

