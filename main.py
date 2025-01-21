import locale
from tabulate import tabulate
from gerar_relatorio import gerar_relatorio_pdf
from src.simulacao import simular_estrutura_capital

# Configurar o locale para moeda brasileira (R$)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Função para formatar valores como moeda ou percentual
def formatar_valor(indicador, valor):
    if "(%)" in indicador:  # Verifica se o indicador é percentual
        return f"{valor:.2f}%"  # Formata como percentual com 2 casas decimais
    else:
        return locale.currency(valor, grouping=True)  # Formata como moeda (R$)

# Solicitar valores do administrador para simulação
print("Bem-vindo ao simulador de rentabilidade!")
capital_proprio = float(input("Informe o valor do Capital Próprio (em R$): "))
capital_terceiros = float(input("Informe o valor do Capital de Terceiros (em R$): "))
taxa_juros_atual = float(input("Informe a taxa de juros da dívida existente (%): "))
nova_divida = float(input("Informe o valor da nova captação (em R$): "))
taxa_juros_nova = float(input("Informe a taxa de juros da nova dívida (%): "))
receita_operacional = float(input("Informe a Receita Operacional esperada (em R$): "))
custos_operacionais = float(input("Informe os Custos Operacionais esperados (em R$): "))
retorno_investimento = float(input("Informe o retorno esperado do investimento da nova dívida (em R$): "))

# Executar a simulação
resultado = simular_estrutura_capital(
    receita_operacional,
    custos_operacionais,
    capital_terceiros,
    taxa_juros_atual,
    nova_divida,
    taxa_juros_nova,
    retorno_investimento
)

# Adicionar informações iniciais à tabela
informacoes_iniciais = [
    ["Capital Próprio", locale.currency(capital_proprio, grouping=True)],
    ["Capital de Terceiros", locale.currency(capital_terceiros, grouping=True)],
    ["Nova Dívida", locale.currency(nova_divida, grouping=True)],
    ["Taxa de Juros da Dívida Existente (%)", f"{taxa_juros_atual:.2f}%"],
    ["Taxa de Juros da Nova Dívida (%)", f"{taxa_juros_nova:.2f}%"],
]

# Formatando os resultados
resultado["Valor"] = resultado.apply(lambda row: formatar_valor(row["Indicador"], row["Valor"]), axis=1)

# Exibir as informações iniciais no terminal
print("\n--- Informações Iniciais ---")
print(tabulate(informacoes_iniciais, headers=["Indicador", "Valor"], tablefmt="grid"))
print("\n--- Resultados da Simulação ---")
print(tabulate(resultado, headers="keys", tablefmt="grid"))

# Adicionar uma análise detalhada para o relatório
analise_detalhada = [
    "1. Lucro Operacional: Representa o lucro gerado antes de considerar os custos financeiros.",
    "2. Custo da Dívida Total: Reflete o custo das dívidas existentes e da nova captação.",
    "3. Lucro Ajustado: Lucro restante após deduzir todos os custos financeiros.",
    "4. Rentabilidade Inicial (%): Mede a eficiência operacional antes de incluir novas dívidas.",
    "5. Rentabilidade Ajustada (%): Avalia a eficiência operacional após considerar a nova captação.",
    "6. ROE Inicial (%): Mostra o retorno sobre o capital próprio antes das novas dívidas.",
    "7. ROE Ajustado (%): Mostra o retorno sobre o capital considerando o impacto da nova captação.",
]

# Gerar o relatório em PDF
gerar_relatorio_pdf(informacoes_iniciais, resultado, analise_detalhada)
