import flet as ft

def markdown(md, size=10):
    """It creates a markdown text with the specified markdown content and the main color of the theme"""
    return ft.Markdown(
        value=md,
        color=ft.Colors.text_color,
        selectable=True,
        latex_style=ft.MarkdownStyle(font_size=size)
    )


def title(text: str, size: int = 24, color=ft.Colors.text_color, weight=ft.FontWeight.BOLD, selectable: bool = True):
    """Texto estilo título (grande y en negrita por defecto)."""
    return ft.Text(text, size=size, color=color, weight=weight, selectable=selectable)


def subtitle(text: str, size: int = 18, color=ft.Colors.text_color, weight=None, selectable: bool = True):
    """Texto estilo subtítulo (mediano)."""
    return ft.Text(text, size=size, color=color, weight=weight, selectable=selectable)


def body(text: str, size: int = 14, color=ft.Colors.text_color, selectable: bool = True):
    """Texto de cuerpo (texto normal)."""
    return ft.Text(text, size=size, color=color, selectable=selectable)


def caption(text: str, size: int = 12, color=ft.Colors.text_color, italic: bool = False):
    """Texto pequeño para captions o notas."""
    return ft.Text(text, size=size, color=color, italic=italic)


def error_text(text: str, size: int = 12, weight=None):
    """Texto para mensajes de error (rojo por defecto si está disponible)."""
    return ft.Text(text, size=size, color=ft.Colors.red_color, weight=weight)


def link(text: str, url: str, size: int = 14, color=ft.Colors.primary, underline: bool = True):
    """Texto estilo enlace (azul por defecto y subrayado)."""
    return ft.Text(
        text,
        size=size,
        color=color,
        underline=underline,
        selectable=True,
        on_click=lambda e: ft.launch(url)
    )

def text_primary_color(text: str, size: int = 14, weight=None, selectable: bool = True):
    """Texto con el color primario del tema."""
    return ft.Text(text, size=size, color=ft.Colors.primary, weight=weight, selectable=selectable)

