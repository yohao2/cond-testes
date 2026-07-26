import streamlit as st
import openpyxl
import dropbox
from dados import condominios
from io import BytesIO
import time

dbx = dropbox.Dropbox(st.secrets["DROPBOX_TOKEN"])

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

def leitura_ibiza():
    st.title('RESIDENCIAL IBIZA')
    st.write(condominios['Residencial Ibiza'])
    st.write('---')

    # checkbox
    st.write('Escolha quais planilhas gerar:')
    checkbox_agua = st.checkbox('Água')
    checkbox_gas = st.checkbox('Gás')

    if checkbox_agua:
        st.subheader('Água')

        # definir data gas 
        data_agua = st.date_input('Data da leitura da água:', value= None, format='DD/MM/YYYY')
        if data_agua:
            dia_mes_agua = data_agua.strftime("%d/%m")

        # definir valor da fatura
        fatura = st.number_input('Valor da fatura (Com multa):')
        # definir valor da multa
        multa = st.number_input('Valor da multa (Deixe em branco caso não haja)')
        # definir nome do arquivo
        nome_arquivo_agua = st.text_input('Digite o nome que quer dar para o arquivo: ')

    if checkbox_gas:
        st.subheader('Gás')

        # definir data gas 
        data_gas = st.date_input('Data da leitura do gás:', value= None, format='DD/MM/YYYY')
        if data_gas:
            dia_mes_gas = data_gas.strftime("%d/%m")

        # definir valores do bujao
        valor_bujao_unidade = st.number_input('Digite o valor UNITÁRIO do bujãos:')
        valor_bujao_total = st.number_input('Digite o valor TOTAL dos bujões:')
        # definir nome do arquivo
        nome_arquivo_gas = st.text_input('Digite o nome que quer dar para o arquivo:')

    st.write('---')

    # definir mes
    mes_referencia = st.selectbox('Mês de referência', ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]).upper()


    # definir leituras
    leitura = st.text_area('Cole a leitura abaixo:')
    leitura = leitura.splitlines()
    botao_gerar = st.button('Gerar')

    lista_agua = []
    lista_gas = []

    agua = 0
    gas = 0

    # formatar leituras
    if botao_gerar:
        for elemento in leitura:
            if elemento == 'ÁGUA':
                agua = 1
            if elemento == 'GÁS':
                gas = 1
                agua = 0

            elemento = elemento[5:]
            
            if elemento != '':
                if agua == 1:
                    elemento = elemento[:4] + ',' + elemento[4:]
                    lista_agua.append(elemento.strip())
                if gas == 1:
                    elemento = elemento[:5] + ',' + elemento[5:]
                    lista_gas.append(elemento.strip())


        if not checkbox_agua and not checkbox_gas:
            st.write('Selecione qual tipo de planilha gerar!')
            st.stop()

        if checkbox_agua:
            if not data_agua or not fatura or not nome_arquivo_agua:
                st.write('Preencha todos os campos!')
                st.stop()

        if checkbox_gas:
            if not data_gas or not valor_bujao_unidade or not valor_bujao_total or not nome_arquivo_gas:
                st.write('Preencha todos os campos!')
                st.stop()

        if not mes_referencia or not leitura:
            st.write('Preencha todos os campos!')
            st.stop()

        st.write('Gerando planilhas...')
        if checkbox_agua: planilha_agua_ibiza(dia_mes_agua, mes_referencia, fatura, multa, lista_agua, nome_arquivo_agua)
        if checkbox_gas: planilha_gas_ibiza(dia_mes_gas, mes_referencia, valor_bujao_unidade, valor_bujao_total, lista_gas, nome_arquivo_gas)

def leitura_bali():
    st.title('RESIDENCIAL BALI')
    st.write(condominios['Residencial Bali'])
    st.write('---')

    # checkbox
    st.write('Escolha quais planilhas gerar:')
    checkbox_agua = st.checkbox('Água')
    checkbox_gas = st.checkbox('Gás', disabled =True)

    if checkbox_agua:
        st.subheader('Água')

        # definir data gas 
        data_agua = st.date_input('Data da leitura da água:', value= None, format='DD/MM/YYYY')
        if data_agua:
            dia_mes_agua = data_agua.strftime("%d/%m")

        # definir valor da fatura
        fatura = st.number_input('Valor da fatura (Com multa):')
        # definir valor da multa
        multa = st.number_input('Valor da multa (Deixe em branco caso não haja)')
        # definir nome do arquivo
        nome_arquivo_agua = st.text_input('Digite o nome que quer dar para o arquivo: ')

    if checkbox_gas:
        st.subheader('Gás')

        # definir data gas 
        data_gas = st.date_input('Data da leitura do gás:', value= None, format='DD/MM/YYYY')
        if data_gas:
            dia_mes_gas = data_gas.strftime("%d/%m")

        # definir valores do bujao
        valor_bujao_unidade = st.number_input('Digite o valor UNITÁRIO do bujãos:')
        valor_bujao_total = st.number_input('Digite o valor TOTAL dos bujões:')
        # definir nome do arquivo
        nome_arquivo_gas = st.text_input('Digite o nome que quer dar para o arquivo: ')

    st.write('---')

    # definir mes
    mes_referencia = st.selectbox('Mês de referência', ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]).upper()


    # definir leituras
    leitura = st.text_area('Cole a leitura abaixo:')
    leitura = leitura.splitlines()
    botao_gerar = st.button('Gerar')

    lista_agua = []
    lista_gas = []

    agua = 0
    gas = 0

    # formatar leituras
    if botao_gerar:
        for elemento in leitura:
            if elemento == 'ÁGUA':
                agua = 1
            if elemento == 'GÁS':
                gas = 1
                agua = 0

            elemento = elemento[5:]
            
            if elemento != '':
                if agua == 1:
                    elemento = elemento[:4] + ',' + elemento[4:]
                    lista_agua.append(elemento.strip())
                if gas == 1:
                    elemento = elemento[:5] + ',' + elemento[5:]
                    lista_gas.append(elemento.strip())


        if not checkbox_agua and not checkbox_gas:
            st.write('Selecione qual tipo de planilha gerar!')
            st.stop()

        if checkbox_agua:
            if not data_agua or not fatura or not nome_arquivo_agua:
                st.write('Preencha todos os campos!')
                st.stop()

        if checkbox_gas:
            if not data_gas or not valor_bujao_unidade or not valor_bujao_total or not nome_arquivo_gas:
                st.write('Preencha todos os campos!')
                st.stop()

        if not mes_referencia or not leitura:
            st.write('Preencha todos os campos!')
            st.stop()

        st.write('Gerando planilhas...')
        if checkbox_agua: planilha_agua_bali(dia_mes_agua, mes_referencia, fatura, multa, lista_agua, nome_arquivo_agua)
        if checkbox_gas: planilha_gas_bali(dia_mes_gas, mes_referencia, valor_bujao_unidade, valor_bujao_total, lista_gas, nome_arquivo_gas)

def planilha_agua_ibiza(dia_mes_agua, mes_referencia, fatura, multa, lista_agua, nome_arquivo):
    wb = openpyxl.load_workbook('arquivos/AGUA IBIZA.xlsx')
    sheet = wb['AGUA']

    # dia do mes
    sheet.cell(row= 2, column = 5).value =  dia_mes_agua
    # mes de referencia
    sheet.cell(row=3, column = 5).value = mes_referencia
    # valor da fatura
    if multa:
        sheet.cell(row=27, column = 5).value = fatura - multa
        # valor da multa
        sheet.cell(row=27, column = 7).value = (f'{fatura} - {multa} DE MULTA')
        
    else: 
        sheet.cell(row=27, column = 5).value = fatura
        sheet.cell(row=27, column = 7).value = 'SEM MULTA'



    # leitura anterior 
    for linha in sheet.iter_rows(min_row=5, max_row = 25, values_only = False):
        linha[1].value = linha[2].value

    # mes de referencia
    sheet.cell(row=5,column=3).value = mes_referencia

    # data leitura
    sheet.cell(row = 6, column = 3).value = dia_mes_agua

    # leitura atual
    for i, valor in enumerate(lista_agua, start= 7):
        sheet.cell(row=i, column = 3).value = valor

    # calculo consumo
    for linha in sheet.iter_rows(min_row = 7, max_row = 25):
        linha[3].value = int(linha[2].value.replace(',','')) - int(linha[1].value.replace(',',''))

        linha[3].value = linha[3].value / 1000

    # verificar valor maior que 5m³
    for linha in sheet.iter_rows(min_row =7, max_row = 25,values_only = False):
        if int(linha[3].value) >= 5:
            linha[5].value = 'MAIOR QUE 5m³'

    # mudar nome da sheet
    wb['AGUA'].title = (mes_referencia)

    salvar_no_dropbox(wb, f'/I. {nome_arquivo}.xlsx')

def planilha_gas_ibiza(dia_mes_gas, mes_referencia, valor_bujao_unidade, valor_bujao_total, lista_gas, nome_arquivo):
    wb = openpyxl.load_workbook('arquivos/GAS IBIZA.xlsx')
    sheet = wb['GAS']

    # dia do mes
    sheet.cell(row= 2, column = 6).value =  dia_mes_gas
    # mes de referencia
    sheet.cell(row=3, column = 6).value = mes_referencia
    # valor por bujão
    sheet.cell(row=7, column = 9).value = valor_bujao_unidade
    # valor da dos bujoes
    sheet.cell(row=27, column = 6).value =  valor_bujao_total

    # leitura anterior 
    for linha in sheet.iter_rows(min_row=5, max_row = 25, values_only = False):
        linha[1].value = linha[2].value
    # mes de referencia
    sheet.cell(row=5,column=3).value = mes_referencia
    # data leitura
    sheet.cell(row = 6, column = 3).value = dia_mes_gas
    # leitura atual
    for i, valor in enumerate(lista_gas, start= 7):
        sheet.cell(row=i, column = 3).value = valor

    # mudar nome da sheet
    wb['GAS'].title = (mes_referencia)
    salvar_no_dropbox(wb, f'/I. {nome_arquivo}.xlsx')

def planilha_agua_bali(dia_mes_agua, mes_referencia, fatura, multa, lista_agua, nome_arquivo):
    wb = openpyxl.load_workbook('arquivos/AGUA BALI.xlsx')
    sheet = wb['AGUA']

    # dia do mes
    sheet.cell(row= 2, column = 5).value =  dia_mes_agua
    # mes de referencia
    sheet.cell(row=3, column = 5).value = mes_referencia
    # valor da fatura
    if multa:
        sheet.cell(row=28, column = 5).value = fatura - multa
        # valor da multa
        sheet.cell(row=28, column = 7).value = (f'{fatura} - {multa} DE MULTA')
        
    else: 
        sheet.cell(row=28, column = 5).value = fatura
        sheet.cell(row=28, column = 7).value = 'SEM MULTA'



    # leitura anterior 
    for linha in sheet.iter_rows(min_row=5, max_row = 26, values_only = False):
        linha[1].value = linha[2].value

    # mes de referencia
    sheet.cell(row=5,column=3).value = mes_referencia

    # data leitura
    sheet.cell(row = 6, column = 3).value = dia_mes_agua

    # leitura atual
    for i, valor in enumerate(lista_agua, start= 7):
        sheet.cell(row=i, column = 3).value = valor

    # calculo consumo
    for linha in sheet.iter_rows(min_row = 7, max_row = 26):
        linha[3].value = int(linha[2].value.replace(',','')) - int(linha[1].value.replace(',',''))

        linha[3].value = linha[3].value / 1000

    # verificar valor maior que 5m³
    for linha in sheet.iter_rows(min_row =7, max_row = 26,values_only = False):
        if int(linha[3].value) >= 5:
            linha[5].value = 'MAIOR QUE 5m³'

    # mudar nome da sheet
    wb['AGUA'].title = (mes_referencia)
    salvar_no_dropbox(wb, f'/B. {nome_arquivo}.xlsx')

def planilha_gas_bali(dia_mes_gas, mes_referencia, valor_bujao_unidade, valor_bujao_total, lista_gas, nome_arquivo):
    wb = openpyxl.load_workbook('arquivos/GAS BALI.xlsx')
    sheet = wb['GAS']

    # dia do mes
    sheet.cell(row= 2, column = 6).value =  dia_mes_gas
    # mes de referencia
    sheet.cell(row=3, column = 6).value = mes_referencia
    # valor por bujão
    sheet.cell(row=7, column = 9).value = valor_bujao_unidade
    # valor da dos bujoes
    sheet.cell(row=28, column = 6).value =  valor_bujao_total

    # leitura anterior 
    for linha in sheet.iter_rows(min_row=5, max_row = 26, values_only = False):
        linha[1].value = linha[2].value
    # mes de referencia
    sheet.cell(row=5,column=3).value = mes_referencia
    # data leitura
    sheet.cell(row = 6, column = 3).value = dia_mes_gas
    # leitura atual
    for i, valor in enumerate(lista_gas, start= 7):
        sheet.cell(row=i, column = 3).value = valor

    # mudar nome da sheet
    wb['GAS'].title = (mes_referencia)
    salvar_no_dropbox(wb, f'B. /{nome_arquivo}.xlsx')

def salvar_leitura_nuvem(nome_arquivo, texto, condominio):

    if condominio == 'Residencial Ibiza':
        dbx.files_upload(
            texto.encode("utf-8"),
            f"/Leituras/Ibiza/{nome_arquivo}.txt",
            mode=dropbox.files.WriteMode.overwrite
        )
    if condominio == 'Residencial Bali':
        dbx.files_upload(
            texto.encode("utf-8"),
            f"/Leituras/Bali/{nome_arquivo}.txt",
            mode=dropbox.files.WriteMode.overwrite
        )

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

        for arquivo in arquivos:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #ccc;
                    border-radius:10px;
                    padding:10px;
                    margin:5px;
                ">
                📄 {arquivo}
                </div>
                """,
                unsafe_allow_html=True
            )
        nova_leitura = st.text_area('Salvar nova leitura:')
        nome_leitura = st.text_input('Nome do arquivo:')
        salvar_leitura = st.button('Salvar')

        if salvar_leitura:
            if not nome_leitura or not nome_leitura:
                st.write('Preencha todos os campos!')
                st.stop()
            salvar_leitura_nuvem(nome_leitura, nova_leitura, escolher_condominio)
            


