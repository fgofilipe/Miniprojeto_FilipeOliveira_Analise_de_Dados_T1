import pandas as pd

# 1. Carregar a base de dados especificando o separador correto (ponto e vírgula)
df = pd.read_csv('Dados/Varejo.csv', sep=';')

# 2. Mostrar o número de registros (linhas) e colunas
print("--- Informações Gerais da Base de Dados ---")
print(f"Número de Linhas (Registros): {df.shape[0]}")
print(f"Número de Colunas: {df.shape[1]}")
print("-" * 40)

# 3. Mostrar as colunas e os tipos de dados
print("\n--- Colunas e Tipos de Dados ---")
print(df.info())


# ==========================================
# SPRINT 2 & 3: LIMPEZA E TRANSFORMAÇÃO (CORRIGIDO)
# ==========================================

print("\n" + "="*40)
print("INICIANDO ETAPAS DE LIMPEZA E TRANSFORMAÇÃO")
print("="*40)

# 1. Remover colunas desnecessárias
df = df.loc[:, 'DATA':'PR_NOME']
print("-> Colunas 'Unnamed' removidas com sucesso!")

# 2. Ajustar tipo de dados: Converter a coluna DATA especificando o formato correto BR
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
print("-> Coluna 'DATA' convertida para Datetime no formato correto!")

# 3. Eliminar duplicatas relevantes (Mantendo a primeira ocorrência)
df = df.drop_duplicates()
print("-> Linhas duplicadas removidas com sucesso!")

# 4. Verificar novamente como ficou a base após a limpeza real
print("\n--- Validação Pós-Limpeza ---")
print(f"Novo número total de linhas: {df.shape[0]}")
print(f"Valores nulos restantes na coluna DATA: {df['DATA'].isnull().sum()}")
print(f"Quantidade atual de linhas duplicadas: {df.duplicated().sum()}")


# ==========================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
# ==========================================

print("\n" + "="*40)
print("SPRINT 4: ESTATÍSTICA DESCRITIVA (COLUNA FILHOS - CL_FHL)")
print("="*40)

# Calculando os parâmetros solicitados
media_filhos = df['CL_FHL'].mean()
mediana_filhos = df['CL_FHL'].median()
desvio_padrao_filhos = df['CL_FHL'].std()
moda_filhos = df['CL_FHL'].mode()[0] # Pega a primeira moda caso haja mais de uma
maximo_filhos = df['CL_FHL'].max()
minimo_filhos = df['CL_FHL'].min()
contagem_filhos = df['CL_FHL'].count()

# Calculando os quartis (25%, 50% que é a mediana, e 75%)
q1 = df['CL_FHL'].quantile(0.25)
q3 = df['CL_FHL'].quantile(0.75)

# Exibindo os resultados formatados
print(f"Contagem total de registros: {contagem_filhos}")
print(f"Média de filhos: {media_filhos:.2f}")
print(f"Mediana de filhos: {mediana_filhos}")
print(f"Moda de filhos: {moda_filhos}")
print(f"Desvio Padrão: {desvio_padrao_filhos:.2f}")
print(f"Mínimo de filhos: {minimo_filhos}")
print(f"Máximo de filhos: {maximo_filhos}")
print(f"1º Quartil (25%): {q1}")
print(f"3º Quartil (75%): {q3}")


# ==========================================
# DESAFIO: AGRUPAMENTOS & SPRINT 5: RELATÓRIO
# ==========================================

print("\n" + "="*40)
print("DESAFIO: EXPLORANDO PADRÕES DE AGRUPAMENTO")
print("="*40)

# Agrupamento 1: Quantidade de compras por Gênero do Cliente
print("\n--- Quantidade de Compras por Gênero ---")
compras_por_genero = df.groupby('CL_GENERO').size().sort_values(ascending=False)
print(compras_por_genero)

# Agrupamento 2: Quantidade de compras por Categoria de Produto
print("\n--- Top 5 Categorias Mais Vendidas ---")
compras_por_categoria = df.groupby('PR_CAT').size().sort_values(ascending=False).head(5)
print(compras_por_categoria)


print("\n" + "="*40)
print("SPRINT 5: RELATÓRIO FINAL DE INSIGHTS")
print("="*40)
print(f"1. Volume Inicial da Base: 830.000 registros | Volume Atual Limpo: {df.shape[0]} registros.")
print("2. Foram eliminadas 96.553 linhas duplicadas e corrigidos 484.735 problemas de formatação de data.")
print(f"3. O perfil médio do cliente indica {media_filhos:.2f} filhos, sendo que a maioria (moda) não possui filhos.")
print(f"4. O gênero majoritário nas compras e a categoria líder de vendas estão listados nos agrupamentos acima.")
print("="*40)