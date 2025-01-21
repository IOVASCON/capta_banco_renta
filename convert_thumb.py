from pdf2image import convert_from_path

# Caminho do arquivo PDF e onde salvar as imagens
pdf_path = "relatorio_rentabilidade.pdf"  # Substitua pelo caminho do seu arquivo
output_folder = "images/"  # Pasta onde as imagens serão salvas
output_image = "relatorio_thumb.png"  # Nome da imagem gerada

# Converter a primeira página do PDF em imagem
pages = convert_from_path(pdf_path, dpi=150)

# Salvar a primeira página como thumbnail
pages[0].save(output_folder + output_image, "PNG")

print(f"Thumbnail gerado em: {output_folder}{output_image}")
