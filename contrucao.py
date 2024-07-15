import flet as ft
import pandas as pd

#Função para ler o arquivo Excel
def read_excel_sheet(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print("Erro ao ler o arquivo Excel:", e)
        return None
    
#Atualização das colunas [mensagem] e [mensagem2]
def update_dataframe(df,mensagem, mensagem2):
    df['Mensagem'] = mensagem
    df['Mensagem2'] = mensagem2
    return df

#Salva as atualizações no arquivo excel
def save_to_excel(df, file_path, sheet_name):
    try:
        with pd.ExcelWriter(file_path, mode='w') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar o arquivo Excel:", e)

#Cria interface 
def main(page: ft.Page):
    page.title = "Editor de Mensagens"
    mensagem_input = ft.TextField(label="Mensagem", value="insira a nova mensagem!")

    #  # Obtendo o primeiro valor da coluna 'Mensagem'
    # df = read_excel_sheet(file_path)
    # if not df.empty:
    #     first_value_mensagem = df.loc[0, 'Mensagem']
    # else:
    #     first_value_mensagem = "Nenhum dado disponível"


    # Criação do DataTable com o primeiro valor
    dataTable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Mensagem atual"))])
    page.add(mensagem_input, dataTable)


    # Criação do DataTable com o primeiro valor
    # dataTable = ft.DataTable(
    #     columns=[
    #         ft.DataColumn(ft.Text("Mensagem atual")) ],
    #     rows=[
    #         ft.DataRow(cells=[ft.DataCell(ft.Text(first_value_mensagem))])
    #     ])
    # page.add(mensagem_input, dataTable, first_value_mensagem)


#Parametros usados pela aplicaçãof
    file_path = 'contatosMay.xlsx'
    sheet_name = 'Planilha1'
    mensagem = 'Boa tarde'
    mensagem2 = 'Chegou a sua vez, aproveite!'

    # df = read_excel_sheet(file_path) # print(df)
    # update_dataframe(df,mensagem, mensagem2) 
    # save_to_excel(df, file_path, sheet_name)

# Iniciar a aplicação Flet
ft.app(target=main)