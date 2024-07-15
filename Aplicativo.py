
# Função para ler o arquivo Excel
# Função para salvar o DataFrame no arquivo Excel
# Função para atualizar o DataFrame com os novos valores
# Função para criar a interface

import flet as ft
import pandas as pd

# Função para ler o arquivo Excel
def read_excel_sheet(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print("Erro ao ler o arquivo Excel:", e)
        return None

# Função para salvar o DataFrame no arquivo Excel
def save_to_excel(df, file_path, sheet_name):
    try:
        with pd.ExcelWriter(file_path, mode='w') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print("Erro ao salvar o arquivo Excel:", e)

# Função para atualizar o DataFrame com os novos valores
def update_dataframe(df, index, mensagem):
    df.at[index, 'Mensagem'] = mensagem
    return df

# Função para criar a interface
def main(page: ft.Page):
    page.title = "Editor de Mensagens"
    
    # Defina o caminho do arquivo Excel e o nome da aba
    file_path = 'contatosMay.xlsx'
    sheet_name = 'Planilha1'
    
    # Ler os dados da aba específica
    df = read_excel_sheet(file_path, sheet_name)
    
    if df is None:
        page.add(ft.Text("Erro ao ler o arquivo Excel."))
        return
    
    # Campos de entrada para as mensagens
    mensagem_input = ft.TextField(label="Mensagem", value="")
    
    # Função de callback para salvar as mensagens
    def save_messages(e):
        nonlocal df
        mensagem = mensagem_input.value
        
        # Atualizar o DataFrame
        df = update_dataframe(df, 0, mensagem)  # Aqui atualizamos a primeira linha (índice 0)
        
        # Salvar no arquivo Excel
        save_to_excel(df, file_path, sheet_name)
    
    # Botão para salvar as mensagens
    save_button = ft.ElevatedButton("Salvar", on_click=save_messages)
    
    # Adicionar os componentes à página
    page.add(mensagem_input, save_button)

# Iniciar a aplicação Flet
ft.app(target=main)

