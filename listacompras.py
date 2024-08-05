import flet as ft
import os

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def main(page: ft.Page):
    # Nome do arquivo txt
    txt_file = "shopping_list.txt"

    # Lista de produtos
    products = []

    def load_data():
        # Carrega os dados do arquivo txt
        if os.path.exists(txt_file):
            with open(txt_file, "r") as file:
                for line in file:
                    name, price = line.strip().split(",")
                    products.append(Product(name, float(price)))
        update_list()

    def save_data():
        # Salva os dados no arquivo txt
        with open(txt_file, "w") as file:
            for product in products:
                file.write(f"{product.name},{product.price}\n")

    def update_list():
        # Atualiza a lista de produtos na interface
        list_view.controls.clear()
        for index, product in enumerate(products):
            list_view.controls.append(
                ft.Row(
                    [
                        ft.Text(product.name),
                        ft.Text(f"{product.price:.2f}"),
                        ft.IconButton(ft.icons.CREATE, on_click=lambda e, i=index: edit_item(i)),
                        ft.IconButton(ft.icons.DELETE, on_click=lambda e, i=index: delete_item(i)),
                    ]
                )
            )
        page.update()

    def add_item(e):
        name = name_input.value
        price = float(price_input.value)
        products.append(Product(name, price))
        name_input.value = ""
        price_input.value = ""
        save_data()
        update_list()

    def delete_item(index):
        del products[index]
        save_data()
        update_list()

    def edit_item(index):
        product = products[index]
        name_input.value = product.name
        price_input.value = str(product.price)
        delete_item(index)
        page.update()

    # Componentes de entrada
    name_input = ft.TextField(label="Nome do Produto", width=200)
    price_input = ft.TextField(label="Valor", width=100)

    # Botão para adicionar item
    add_button = ft.ElevatedButton("Adicionar", on_click=add_item)

    # Lista de itens
    list_view = ft.ListView(expand=True)

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Row([name_input, price_input, add_button], alignment="center"),
                list_view,
            ]
        )
    )

    load_data()

ft.app(target=main)