import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Classificação de Veículos",
    layout="wide"
)

@st.cache_data
def carregar_dados_e_modelo():
    dados_carros = pd.read_csv("car.csv")
    encoder = OrdinalEncoder()

    for col in dados_carros.columns.drop('class'):
        dados_carros[col] = dados_carros[col].astype('category')

    X_encoded = encoder.fit_transform(dados_carros.drop('class', axis=1))

    y = dados_carros['class'].astype('category').cat.codes

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

    modelo = RandomForestClassifier()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    acuracia = accuracy_score(y_test, y_pred)

    return encoder, modelo, acuracia, dados_carros

encoder, modelo, acuracia, dados_carros = carregar_dados_e_modelo()

st.title("Previsão de Qualidade de Veículo")
st.write(f"Acurácia do modelo: {acuracia:.0%}")

input_features = [
    st.selectbox("Preço:", dados_carros['buying'].unique()),
    st.selectbox("Manutenção:", dados_carros['maint'].unique()),
    st.selectbox("Portas:", dados_carros['doors'].unique()),
    st.selectbox("Capacidade de Passageiros:", dados_carros['persons'].unique()),
    st.selectbox("Porta Malas:", dados_carros['lug_boot'].unique()),
    st.selectbox("Segurança:", dados_carros['safety'].unique())
]

processar = st.button("Processar")
if processar:
    dados = pd.DataFrame([input_features], columns=dados_carros.columns.drop('class'))
    dados_codificados = encoder.transform(dados)
    previsao_codificada = modelo.predict(dados_codificados)
    previsao = dados_carros['class'].astype('category').cat.categories[previsao_codificada][0]
    if previsao == "unacc":
        previsao = "Ruim"
    elif previsao == "acc":
        previsao = "Aceitável"
    elif previsao == "good":
        previsao = "Bom"
    else:
        previsao = "Muito bom"
    st.header(f"Qualidade do Veículo: {previsao}")