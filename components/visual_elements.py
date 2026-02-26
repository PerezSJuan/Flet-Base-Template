import flet as ft

def card(content=[]):
    """It creates a card with the main color of the theme and a shadow"""
    return ft.Card(
        bgcolor=ft.Colors.surface,
        shadow=ft.Shadow(blur_radius=5, color=ft.Colors.shadow_color),
        content=ft.Container(
            width=400,
            padding=15,
            content=ft.Column(
                controls=content, 
                spacing=20,
            )
        )
    )


def expansion_panel(title, content=[], expanded=False):
    """It creates an expansion panel with the specified title and content and the main color of the theme"""
    return ft.ExpansionPanel(
        header=ft.Text(title, color=ft.Colors.text_color),
        content=ft.Column(controls=content, spacing=10),
        expanded=expanded,
        bgcolor=ft.Colors.surface,
        content_bgcolor=ft.Colors.surface,
        border_color=ft.Colors.border_color,
    )

