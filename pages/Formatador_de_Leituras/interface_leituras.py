import streamlit as st
from dados import condominios
from planilhas_leituras import planilha_agua_ibiza, planilha_gas_ibiza, planilha_agua_bali, planilha_gas_bali
from dropbox_utils import dbx, salvar_no_dropbox



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


