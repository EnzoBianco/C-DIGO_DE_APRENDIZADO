faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas
imposto =  faturamento * 0.10
lucro = faturamento - custo - imposto
print(faturamento)
print(lucro)
margem_lucro = lucro / faturamento
print(margem_lucro)
print(margem_lucro * 100)

restituicao = imposto * 0.10
print(restituicao)
restituicao = faturamento * 0.10 * 0.10


tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")