faturamento = 1200
custo = 370

novas_vendas = 700
faturamento = faturamento + novas_vendas

taxa_imposto = 0.10 # 10% sendo tranformado em decimal (float)
mensagem = "O faturamento foi de" # texto (string)
teve_lucro = False # booleano

imposto = faturamento * taxa_imposto

print("Faturamento: ", faturamento)
print("Custo: ", custo)
print("Lucro: ", faturamento - custo - imposto)
print(mensagem, faturamento)

