import dropbox
from io import BytesIO
import time
import streamlit as st

def salvar_no_dropbox(wb, nome_arquivo):
    # definindo bytesIO() como arquivo
    # bytesIO: guarda os bytes do que for passado, nesse caso da planilha do excel
    arquivo = BytesIO()

    # salvando a planilha dentro de bytesIO
    wb.save(arquivo)
    # lendo o arquivo desde o inicio
    arquivo.seek(0)

    # salvar no dropbox
    dbx.files_upload(
        # passando o arquivo a ser salvo
        arquivo.read(),
        # qual o nome que o arquivo vai ter
        nome_arquivo,
        # definindo o que fazer, writemode: para escrever o arquivo no dropbox
        mode=dropbox.files.WriteMode.add
    )

    time.sleep(1)


def listar_leituras(condominio):

    if condominio == "Residencial Ibiza":
        pasta = "/Leituras/Ibiza"

    elif condominio == "Residencial Bali":
        pasta = "/Leituras/Bali"

    else:
        return []

    resultado = dbx.files_list_folder(pasta)

    arquivos = []

    for arquivo in resultado.entries:
        if arquivo.name.endswith(".txt"):
            arquivos.append(
                arquivo.name.replace(".txt", "")
            )

    return arquivos


dbx = dropbox.Dropbox(
    oauth2_refresh_token=st.secrets["DROPBOX_REFRESH_TOKEN"],
    app_key=st.secrets["DROPBOX_APP_KEY"],
    app_secret=st.secrets["DROPBOX_APP_SECRET"]
)

