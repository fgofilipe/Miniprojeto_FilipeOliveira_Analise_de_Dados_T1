# Mini-Projeto Avaliativo: Análise Exploratória de Dados em Base de Varejo

Turma: Analise_de_Dados_T1  
Estudante: Filipe de Oliveira Gomes  

---

# Sobre o Projeto

Este projeto foi desenvolvido como atividade avaliativa do curso de Análise de Dados do SENAI, com o objetivo de aplicar conceitos fundamentais de manipulação, limpeza, transformação e exploração de dados utilizando Python.

A análise foi realizada sobre uma base de dados de varejo contendo milhares de registros de compras, clientes e categorias de produtos.

O projeto utiliza:
- leitura estruturada de arquivos CSV;
- tratamento de inconsistências;
- conversão de tipos de dados;
- estatística descritiva;
- agrupamentos analíticos;
- geração de gráficos;
- e extração de insights estratégicos.

---

# Objetivos do Projeto

- Aplicar técnicas de Análise Exploratória de Dados (AED);
- Manipular arquivos CSV utilizando Python;
- Utilizar estruturas condicionais para tratamento de dados;
- Trabalhar com conversão e validação de datas;
- Explorar estatísticas descritivas;
- Identificar padrões através de agrupamentos;
- Desenvolver organização e versionamento com Git e GitHub.

---

# Tecnologias Utilizadas

- Python 3
- Pandas
- CSV (módulo nativo do Python)
- Matplotlib
- VS Code
- Git
- GitHub

---

# Como Executar o Projeto

# Pré-requisitos

Antes de executar o projeto, certifique-se de possuir instalado:

- Python 3
- pip

---

## Instalação das Dependências

Instale as bibliotecas necessárias com:

```bash
pip install pandas matplotlib
```

Ou utilize:

```bash
pip install -r requirements.txt
```

---

## Executando o Projeto

No terminal, execute:

```bash
python script_projeto.py
```

---

# Etapas Desenvolvidas

---

## Sprint 1 — Importação dos Dados

Nesta etapa foi realizada:

- Leitura estruturada da base utilizando `csv.DictReader`;
- Conversão da estrutura para `DataFrame`;
- Verificação inicial da base de dados;
- Identificação da quantidade de linhas e colunas.

---

## Sprint 2 — Limpeza de Dados

Foram aplicadas técnicas de:

- Remoção de colunas irrelevantes;
- Tratamento de categorias vazias;
- Conversão de dados inválidos;
- Remoção de registros duplicados.


---

## Sprint 3 — Transformação de Dados

Nesta etapa foi realizada:

- Conversão da coluna `DATA` para o tipo `datetime`;
- Validação de datas inválidas com `errors='coerce'`;
- Remoção de registros com inconsistências temporais;
- Conversão de dados numéricos utilizando `pd.to_numeric()`.

---

## Sprint 4 — Estatística Descritiva

Foi realizada análise estatística da coluna `CL_FHL` (quantidade de filhos), incluindo:

- Média
- Mediana
- Moda
- Desvio padrão
- Quartis
- Valores mínimo e máximo

Essas métricas permitiram identificar o perfil médio dos clientes da base.

---

## Sprint 5 — Agrupamentos Analíticos

Foram realizados agrupamentos para identificar padrões de comportamento:

# Compras por gênero
Análise da participação de cada gênero no volume de compras.

# Categorias mais vendidas
Identificação das categorias com maior quantidade de vendas.

# Compras por mês
Análise temporal do comportamento de consumo.

---

# Visualização Gráfica

O projeto gera um gráfico de barras utilizando `Matplotlib` para representar visualmente as categorias mais vendidas da base.

A visualização auxilia na interpretação rápida dos padrões comerciais encontrados.

---

# Principais Insights Encontrados

- A base original possuía milhares de registros duplicados que foram removidos durante o tratamento;
- Foram identificadas inconsistências de datas e tratadas utilizando o módulo `datetime`;
- A maior parte dos clientes não possui filhos;
- O setor de ALIMENTOS apresentou o maior volume de vendas da base;
- O público feminino demonstrou maior participação nas compras realizadas;
- A limpeza dos dados melhorou significativamente a confiabilidade das análises.

---

# Versionamento

O projeto foi versionado utilizando Git e hospedado no GitHub para controle de alterações, organização do desenvolvimento e rastreabilidade das modificações realizadas.

---

# Aluno

*Filipe de Oliveira Gomes*

🔗 GitHub:  
https://github.com/fgofilipe
