import pandas as pd

def simular_estrutura_capital(
    receita_operacional,
    custos_operacionais,
    divida_atual,
    taxa_juros_atual,
    nova_divida,
    taxa_juros_nova,
    retorno_investimento
):
    """
    Realiza a simulação dos indicadores financeiros.
    """
    # Cálculo do lucro operacional antes das dívidas
    lucro_operacional = receita_operacional - custos_operacionais

    # Cálculo dos custos financeiros
    custo_divida_existente = divida_atual * (taxa_juros_atual / 100)
    custo_nova_divida = nova_divida * (taxa_juros_nova / 100)

    # Lucro operacional ajustado após as dívidas
    lucro_ajustado = lucro_operacional - custo_divida_existente - custo_nova_divida + retorno_investimento

    # Rentabilidade sobre a receita
    rentabilidade_inicial = (lucro_operacional - custo_divida_existente) / receita_operacional * 100
    rentabilidade_ajustada = lucro_ajustado / receita_operacional * 100

    # Retorno sobre o capital próprio (ROE)
    capital_total = divida_atual + nova_divida
    roe_inicial = (lucro_operacional - custo_divida_existente) / (divida_atual / 2) * 100
    roe_ajustado = lucro_ajustado / (capital_total / 2) * 100

    # Montar o DataFrame dos resultados
    resultado = {
        "Indicador": [
            "Lucro Operacional",
            "Custo da Dívida Total",
            "Lucro Ajustado",
            "Rentabilidade Inicial (%)",
            "Rentabilidade Ajustada (%)",
            "ROE Inicial (%)",
            "ROE Ajustado (%)",
        ],
        "Valor": [
            lucro_operacional,
            custo_divida_existente + custo_nova_divida,
            lucro_ajustado,
            rentabilidade_inicial,
            rentabilidade_ajustada,
            roe_inicial,
            roe_ajustado,
        ],
    }

    return pd.DataFrame(resultado)
