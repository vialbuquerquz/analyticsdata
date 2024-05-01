import pandas as pd



data = pd.read_excel("Trilha Impressione no Trabalho - Aula 1.xlsx")


filterestoque = data[(data['Estoque'] < 5000)] #mostrando estoques menores que 5k
print(filterestoque)

paisdeorigem = data[(data['Origem'] == 'China')]
print(paisdeorigem)

#contando quantas vezes uma marca se repete na planilha, ou seja, a quantidade de produtos que determinada marca vendeu.
consultaDeMarcas = 'Mega Peças'
contagem = data['Marca'].value_counts().get(consultaDeMarcas, 0)
print(f"O número em que a marca {consultaDeMarcas} se repete é de {contagem} vezes.")

