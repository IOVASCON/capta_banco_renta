from fpdf import FPDF
from datetime import datetime

# Classe para criar o PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Rentabilidade - Simulação Financeira', border=0, ln=1, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

# Função para criar o relatório
def gerar_relatorio_pdf(informacoes_iniciais, resultados, analise):
    pdf = PDF()
    pdf.add_page()

    # Cabeçalho
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Data: {datetime.today().strftime("%d/%m/%Y")}', ln=1, align='R')
    pdf.ln(5)

    # Endereçamento
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Para: Administrador da Empresa XYZ', ln=1)
    pdf.cell(0, 10, 'De: Departamento Financeiro', ln=1)
    pdf.ln(10)

    # Informações iniciais
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Informações Iniciais', ln=1)
    pdf.set_font('Arial', '', 12)
    for linha in informacoes_iniciais:
        pdf.cell(0, 10, f'{linha[0]}: {linha[1]}', ln=1)
    pdf.ln(10)

    # Resultados da simulação
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Resultados da Simulação', ln=1)
    pdf.set_font('Arial', '', 12)
    for index, row in resultados.iterrows():
        indicador = row["Indicador"]
        valor = row["Valor"]
        
        # Remove a duplicidade do "%" no momento de adicionar ao PDF
        if "(%)" in indicador:
            valor = valor.replace("%%", "%")
        
        pdf.cell(0, 10, f'{indicador}: {valor}', ln=1)
    pdf.ln(10)


    # Análise detalhada
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Análise Detalhada', ln=1)
    pdf.set_font('Arial', '', 12)
    
    # Adicionando análises item por item
    pdf.multi_cell(0, 10, "1. Lucro Operacional:\n"
                          "O lucro operacional da empresa foi de R$ 500.000,00, indicando uma "
                          "boa capacidade de geração de lucros antes de custos financeiros e impostos.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "2. Custo da Dívida Total:\n"
                          "O custo total da dívida foi de R$ 95.000,00, composto por R$ 50.000,00 (juros da dívida existente a 10%) "
                          "e R$ 45.000,00 (juros da nova dívida a 15%). Esse custo representa 19% do lucro operacional.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "3. Lucro Ajustado:\n"
                          "O lucro ajustado após o custo da dívida foi de R$ 505.000,00. Esse valor mostra que, "
                          "apesar dos custos financeiros, a empresa ainda mantém uma rentabilidade saudável.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "4. Rentabilidade Inicial (%):\n"
                          "A rentabilidade inicial foi de 30,00%, calculada antes de considerar os custos das dívidas adicionais. "
                          "Isso reflete uma operação eficiente com boa margem sobre a receita operacional.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "5. Rentabilidade Ajustada (%):\n"
                          "Após considerar o custo da dívida e o retorno esperado do investimento, a rentabilidade ajustada foi de 33,67%. "
                          "O aumento em relação à rentabilidade inicial demonstra que o retorno do investimento foi positivo.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "6. ROE Inicial (%):\n"
                          "O ROE inicial, ou retorno sobre o capital próprio antes de incluir novas dívidas, foi de 180,00%. "
                          "Esse alto valor indica uma excelente eficiência no uso do capital dos acionistas.")
    pdf.ln(5)

    pdf.multi_cell(0, 10, "7. ROE Ajustado (%):\n"
                          "Após considerar o impacto da nova dívida, o ROE ajustado foi de 126,25%. Embora tenha diminuído em relação ao ROE inicial, "
                          "esse valor ainda reflete um retorno muito atrativo, validando a decisão de captação.")
    pdf.ln(10)
    
    # Outra opção do PARECER do relatório
    # for linha in analise:
    #    pdf.multi_cell(0, 10, linha)
    # pdf.ln(10)

    # Rodapé
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 10, 'Este relatório foi gerado automaticamente pelo simulador de rentabilidade.', ln=1, align='C')

    # Salvar o PDF
    pdf.output('relatorio_rentabilidade.pdf')
    print("Relatório gerado com sucesso: relatorio_rentabilidade.pdf")
