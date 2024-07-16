import flet as ft
import pandas as pd
import time

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

# Função para mostrar a tela de carregamento
def show_loading_screen(page: ft.Page):
    logo_path = "images/logo.png"  # Substitua pelo caminho da sua logo
    spinner = ft.ProgressRing(width=150, height=150, stroke_width=10, color=ft.colors.GREEN_ACCENT_700)
    logo_widget = ft.Image(src=logo_path, width=120, height=120)
 
    loading_screen = ft.Container(
        width=page.window_width,
        height=page.window_height,
        content=ft.Stack(
            [
                ft.Container(
                    content=logo_widget,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=spinner,
                    alignment=ft.alignment.center
                )
            ],
            expand=True
        ))

    page.add(loading_screen)
    page.update()

    # Simula um processo de carregamento (exemplo: leitura de arquivo)
    file_path = 'contatosMay.xlsx'
    df = read_excel_sheet(file_path)
    time.sleep(3)  
    page.remove(loading_screen)
    show_main_content(page, df)

# Função para mostrar o conteúdo principal (interface de edição de mensagens)
def show_main_content(page: ft.Page, df: pd.DataFrame):
    if df is not None and not df.empty:
        first_value_mensagem = df.loc[0, 'Mensagem']
        first_value_mensagem2 = df.loc[0, 'Mensagem2']
    else:
        first_value_mensagem = "Nenhum dado disponível"
        first_value_mensagem2 = "Nenhum dado disponível"

    page.title = "Editor de Mensagens"
    mensagem_input = ft.TextField(
        label="Editar mensagem", 
        value=first_value_mensagem,
        bgcolor=ft.colors.BLUE_GREY_800,
        color=ft.colors.WHITE,
        label_style=ft.TextStyle(color=ft.colors.GREEN_ACCENT_700),
        border_color=ft.colors.GREEN_ACCENT_700,
        multiline=True
    )
    mensagem_input2 = ft.TextField(
        label="Editar mensagem 2", 
        value=first_value_mensagem2,
        bgcolor=ft.colors.BLUE_GREY_800,
        color=ft.colors.WHITE,
        label_style=ft.TextStyle(color=ft.colors.GREEN_ACCENT_700),
        border_color=ft.colors.GREEN_ACCENT_700,
        multiline=True,
    )

    file_path = 'contatosMay.xlsx'
    sheet_name = 'Planilha1'

    def on_save_click(e):
        updated_df = update_dataframe(df, mensagem_input.value, mensagem_input2.value)
        save_to_excel(updated_df, file_path, sheet_name)

    def on_confirm_send(e):
        confirm_dialog = ft.BottomSheet(
            on_dismiss=on_confirm_send,
            content=ft.Container(
                adding=50,
                content=ft.Column(
                tight=True,
                controls=[
            title="Confirmar Envio",
            content="Deseja realmente enviar as mensagens?",
            actions=[
                ft.BottomSheet(text="Cancelar", on_click=lambda e: confirm_dialog()),
                ft.BottomSheet(text="Ok", on_click=lambda e: send_messages())
            ]
        )
        page.add(confirm_dialog)

    def send_messages():
        # Implementar a lógica de envio das mensagens aqui
        print("Mensagens enviadas com sucesso!")

    save_button = ft.ElevatedButton(text="Salvar", on_click=on_save_click)
    send_button = ft.ElevatedButton(text="Enviar", on_click=on_confirm_send)

    page.add(mensagem_input, mensagem_input2, save_button, send_button)

# Função principal que inicia a aplicação Flet
def main(page: ft.Page):
    page.window_width = 375
    page.window_height = 667
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    
    # Exibe a tela de carregamento inicial
    show_loading_screen(page)

# Iniciar a aplicação Flet
ft.app(target=main)