import matplotlib.pyplot as plt
import numpy as np


mes = np.arange(12) + 1 # meses de 1 a 12

# quantidades de produtos vendidos por mês
creme_facial = np.array([ 2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900 ])
limpeza_facial = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])
pasta_dentaria = np.array([ 5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400 ])
sabonete = np.array([ 9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400 ])
shampoo = np.array([ 1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800 ])
hidratante = np.array([ 1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760 ])

total = creme_facial + limpeza_facial + pasta_dentaria + sabonete + shampoo + hidratante


# Gráfico 1 - Total de produtos Vendidos por mês - Linha
plt.plot(total)
plt.xticks(mes)
plt.xlabel("Mês")
plt.title("Total de produtos vendidos")
plt.show()


# Gráfico 2 - Gráfico com todos os produtos vendidos por mês - Linha
produtos = ['Creme Facial', 'Limpeza Facial', 'Pasta Dentária', 'Sabonete', 'Shampoo', 'Hidratante']

plt.plot(mes, creme_facial, label='Creme Facial')
plt.plot(mes, limpeza_facial, label='Limpeza Facial')
plt.plot(mes, pasta_dentaria, label='Pasta Dentária')
plt.plot(mes, sabonete, label='Sabonete')
plt.plot(mes, shampoo, label='Shampoo')
plt.plot(mes, hidratante, label='Hidratante')

plt.xticks(mes)
plt.title("Produtos Vendidos por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade Vendida")
plt.legend()
plt.show()


# Gráfico 3 - Comparativo de Creme Facial com Limpeza Facial por mês - Barras
plt.bar(mes - 0.2, creme_facial, width=0.4, label='Creme Facial')
plt.bar(mes + 0.2, limpeza_facial, width=0.4, label='Limpeza Facial')

plt.xticks(mes)
plt.title("Vendas mensais de creme facial e limpeza facial")
plt.xlabel("Mês")
plt.ylabel("Quantidade Vendida")
plt.legend()
plt.show()


# Gráfico 4 - Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos (1000-1999, 2000-2999, ...)
faixas = [1000, 2000, 3000, 4000, 5000, 6000]
Hcreme_facial = np.histogram(creme_facial, bins=faixas)[0]
Hlimpeza_facial = np.histogram(limpeza_facial, bins=faixas)[0]

plt.bar(faixas[:-1], Hcreme_facial, width=1000, label='Creme Facial')
plt.bar(faixas[:-1], Hlimpeza_facial, width=1000, label='Limpeza Facial')

plt.xlabel("Faixa de Quantidade de Produtos Vendidos")
plt.ylabel("Quantidade de Meses")
plt.title("Histograma de quantidade de meses (y) e faixas de quantidades de produtos vendidos")
plt.legend()
plt.show()


# Gráfico 5 - Pizza. % da quantidade produtos vendidos no ano em cada produto
total_creme_facial = np.sum(creme_facial)
total_limpeza_facial = np.sum(limpeza_facial)
total_pasta_dentaria = np.sum(pasta_dentaria)
total_sabonete = np.sum(sabonete)
total_shampoo = np.sum(shampoo)
total_hidratante = np.sum(hidratante)

produtos = ['Creme Facial', 'Limpeza Facial', 'Pasta Dentária', 'Sabonete', 'Shampoo', 'Hidratante']

totais = [total_creme_facial, total_limpeza_facial, total_pasta_dentaria, total_sabonete, total_shampoo, total_hidratante]

plt.pie(totais, labels=produtos, autopct='%1.1f%%', startangle=140)
plt.title("% da quantidade de produtos vendidos no Ano por produto")

plt.show()