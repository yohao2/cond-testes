import streamlit as st
import openpyxl
import dropbox
from dados import condominios
from io import BytesIO
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from dropbox_utils import salvar_no_dropbox
from Formatador_de_Leituras.interface_leituras import *
from dropbox_utils import salvar_no_dropbox




st.set_page_config(layout="wide")

esquerda, direita = st.columns([2,1])

with esquerda:

    # selecionar condominios
    with st.sidebar:
        escolher_condominio = st.selectbox('Selecione um Condomínio', condominios, index = None, placeholder= '...')

    # aviso condominio nao selecionado
    if not escolher_condominio:
        st.title('SELECIONE UM CONDOMÍNIO!')
        st.stop()

    # funcoes para chamar condominio
    funcoes = {
        'Residencial Ibiza': leitura_ibiza,
        'Residencial Bali': leitura_bali
    }

    # rodar condominio selecionado
    if escolher_condominio in funcoes:
        funcoes[escolher_condominio]()

with direita:
    espaco1, centro, espaco2 = st.columns([1, 2, 1])

    with centro:
        st.subheader('Leituras Anteriores')

        arquivos = listar_leituras(escolher_condominio)
        if not arquivos:
            st.write('Nenhuma Leitura Salva...')

        for arquivo in arquivos:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #ccc;
                    border-radius:8px;
                    padding:3px 8px;
                    margin:2px;
                ">
                📄 {arquivo}
                </div>
                """,
                unsafe_allow_html=True
            )

        if "nova_leitura_aberta" not in st.session_state:
            st.session_state.nova_leitura_aberta = False


        if st.button("Nova Leitura"):
            st.session_state.nova_leitura_aberta = True


        if st.session_state.nova_leitura_aberta:

            nova_leitura = st.text_area("Leitura:")
            nome_leitura = st.text_input("Nome do arquivo:")

            if st.button("Salvar"):

                if not nome_leitura or not nova_leitura:
                    st.write("Preencha todos os campos!")

                else:
                    salvar_no_dropbox(
                        nome_leitura,
                        nova_leitura,
                        escolher_condominio
                    )

                    st.success("Leitura salva!")
                    st.stop()