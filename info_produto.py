codigo = input("Digite o código do produto: ")
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

valor_total = quantidade * preco

print("\nInformações do produto:")
print("Código:", codigo)
print("Nome:", nome_produto)
print("Quantidade:", quantidade)
print("Preço unitário:", preco)
print("Valor total da compra:", valor_total)
