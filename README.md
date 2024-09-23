# Previsão de Qualidade de Veículos
Este projeto tem como objetivo prever a qualidade de um veículo com base em suas características. A previsão pode ser utilizada para ajudar a definir a qualidade de um veículo e realizar análises sobre a demanda de manutenção.

### Objetivo
O sistema utiliza características dos veículos para prever a qualidade, categorizando como "Ruim", "Aceitável", "Bom" ou "Muito bom". Essas informações podem ser úteis para estimar a demanda esperada e tomar decisões mais informadas.

### Funcionalidades
- Entrada de dados como características do veículo (preço, manutenção, portas, capacidade de passageiros, etc.).
- Previsão da qualidade do veículo com base em algoritmos de aprendizado de máquina.
- Acurácia do modelo baseada em dados históricos de veículos.

### Tecnologias Utilizadas
- Python para desenvolvimento geral.
- Scikit-learn para construção e avaliação do modelo de Machine Learning.
- Streamlit para interface gráfica e interação com o usuário.
- Random Forest Classifier como algoritmo de previsão.

### Como Executar
1. Clone o repositório:
`git clone https://github.com/giovani-bruno/prever_qualidade_do_carro.git`

2.Instale as dependências:
`pip install -r requirements.txt`

3. Execute a aplicação:
`streamlit run app.py`

Insira as características do veículo para obter a previsão da qualidade.
