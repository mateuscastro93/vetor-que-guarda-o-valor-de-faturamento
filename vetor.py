import json


with open('dados_faturamento.json') as arquivo:
    dados_faturamento = json.load(arquivo)


menor_faturamento = min(dados_faturamento)
maior_faturamento = max(dados_faturamento)

dias_com_faturamento = [faturamento for faturamento in dados_faturamento if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = sum(faturamento > media_mensal for faturamento in dados_faturamento)

print("Menor faturamento diário:", menor_faturamento)
print("Maior faturamento diário:", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)
