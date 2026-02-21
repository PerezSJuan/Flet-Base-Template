"""
ejemplo_simple.py
=================
Ejemplo minimalista: app con solo barra superior y contenido.

Demuestra:
    - Uso básico de LayoutBuilder con una sola barra
    - Helper setup_responsive_layout()
    - Helper create_simple_navbar()
"""

import flet as ft
from layout_system import LayoutBuilder
from layout_helpers import create_simple_navbar, setup_responsive_layout


def main(page: ft.Page):
    page.title = "Ejemplo Simple - Flet Layout"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # Contenido principal
    content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("¡Bienvenido!", size=32, weight=ft.FontWeight.BOLD),
                ft.Text("Este es un layout simple con solo barra superior.", size=16),
                ft.Divider(height=20),
                ft.Text(
                    "Redimensiona la ventana para ver el comportamiento responsive.",
                    italic=True,
                    color=ft.Colors.GREY_600,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Acción 1", icon=ft.Icons.PLAY_ARROW),
                        ft.ElevatedButton("Acción 2", icon=ft.Icons.SAVE),
                        ft.ElevatedButton("Acción 3", icon=ft.Icons.SEARCH),
                    ],
                    wrap=True,
                    spacing=10,
                ),
            ],
            spacing=16,
        ),
        padding=30,
        expand=True,
    )

    # Navbar
    navbar = create_simple_navbar("Mi App", show_menu=False)

    # Layout
    layout = (
        LayoutBuilder()
        .with_content(content)
        .with_top_bar(navbar, height=60, bgcolor=ft.Colors.BLUE_700)
        .build()
    )

    page.add(layout)
    setup_responsive_layout(layout, page)


if __name__ == "__main__":
    ft.app(target=main)
