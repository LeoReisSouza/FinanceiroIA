import flet as ft
from agent import FinancialAgent
from dotenv import load_dotenv
import os

load_dotenv()

class ChatMessage(ft.Container):
    def __init__(self, message: dict):
        super().__init__()
        self.message = message

        self.content = ft.Column(
            [
                ft.Text(
                    self.message["role"],
                    weight="bold",
                    color=ft.Colors.BLUE_700 if self.message["role"] == "Agente" else ft.Colors.GREEN_700,
                ),
                ft.Text(self.message["content"], selectable=True),
            ],
            tight=True,
            spacing=5,
        )
        self.padding = 10
        self.margin = 5
        self.border_radius = 10
        self.bgcolor = ft.Colors.GREY_100 if self.message["role"] == "Agente" else ft.Colors.GREY_300
        self.border = ft.border.all(1, "grey")


def main(page: ft.Page):
    page.title = "Agente Financeiro AI"
    financial_agent = FinancialAgent()
    chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    new_message = ft.TextField(
        hint_text="Digite sua pergunta financeira aqui...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    def send_click(e):
        if not new_message.value.strip():
            return

        pergunta = new_message.value.strip()
        print(f"Pergunta recebida: {pergunta}")  # Log no console

        user_msg = {"role": "Você", "content": pergunta}
        chat.controls.append(ChatMessage(user_msg))

        processing_msg = {"role": "Agente", "content": "Processando..."}
        placeholder = ChatMessage(processing_msg)
        chat.controls.append(placeholder)

        new_message.value = ""
        page.update()

        try:
            print("Enviando para o agente...")
            resposta = financial_agent.query(pergunta)
            print(f"Resposta recebida: {resposta}")

            chat.controls.remove(placeholder)
            chat.controls.append(ChatMessage({"role": "Agente", "content": resposta}))
        except Exception as e:
            print(f"Erro: {str(e)}")
            chat.controls.remove(placeholder)
            chat.controls.append(ChatMessage({"role": "Agente", "content": f"Erro: {str(e)}"}))

        page.update()

    page.add(
        ft.Column([
            ft.Text("Assistente Financeiro AI", size=20, weight="bold"),
            ft.Container(
                content=chat,
                border=ft.border.all(1, "grey"),
                border_radius=10,
                padding=10,
                expand=True,
            ),
            ft.Row([
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    on_click=send_click,
                ),
            ]),
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
