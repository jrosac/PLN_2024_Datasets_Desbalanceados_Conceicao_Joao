import pandas as pd

# Função para filtrar o CSV
def filtrar_csv(arquivo_entrada, arquivo_saida):
    # Lê o arquivo CSV
    df = pd.read_csv(arquivo_entrada)
    
    # Filtra as linhas onde a coluna 'label' tem o valor 0
    df_filtrado = df[df['label'] == 1]
    
    # Gera um novo CSV com os dados filtrados
    df_filtrado.to_csv(arquivo_saida, index=False)

# Caminho do arquivo de entrada e saída
arquivo_entrada = '/home/jrosa/Documentos/UFS/PLN/PLN_2024_Datasets_Desbalanceados_Conceicao_Joao/Dataset/email_text.csv'  # Substitua pelo nome do seu arquivo de entrada
arquivo_saida = 'dataset_filtrado2.csv'  # Nome do arquivo de saída

# Chama a função para filtrar o CSV
filtrar_csv(arquivo_entrada, arquivo_saida)
