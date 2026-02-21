"""
layout_helpers.py
=================
Funciones auxiliares para simplificar el uso del sistema de layouts.

Funciones:
    setup_responsive_layout: Configura el resize automático.
    create_simple_navbar:     Crea una barra de navegación simple.
    create_simple_sidebar:    Crea un sidebar con ítems de navegación.
    create_footer:            Crea un pie de página simple.
    validate_layout_params:   Valida parámetros de dimensiones.
"""

import flet as ft
from typing import Callable, List, Optional

from layout_system import ResponsiveLayout


def validate_layout_params(
    left_bar_width: Optional[int] = None,
    right_bar_width: Optional[int] = None,
    top_bar_height: Optional[int] = None,
    bottom_bar_height: Optional[int] = None,
) -> None:
    """
    Valida que los parámetros de dimensiones estén en rangos razonables.

    Args:
        left_bar_width:   Ancho de la barra izquierda (50–1000 px).
        right_bar_width:  Ancho de la barra derecha (50–1000 px).
        top_bar_height:   Altura de la barra superior (30–200 px).
        bottom_bar_height: Altura de la barra inferior (30–200 px).

    Raises:
        ValueError: Si algún valor está fuera de su rango permitido.
    """
    constraints = [
        (left_bar_width, "left_bar_width", 50, 1000),
        (right_bar_width, "right_bar_width", 50, 1000),
        (top_bar_height, "top_bar_height", 30, 200),
        (bottom_bar_height, "bottom_bar_height", 30, 200),
    ]
    for value, name, min_v, max_v in constraints:
        if value is not None and not (min_v <= value <= max_v):
            raise ValueError(
                f"'{name}' debe estar entre {min_v} y {max_v} px. Valor recibido: {value}"
            )


def setup_responsive_layout(layout: ResponsiveLayout, page: ft.Page) -> None:
    """
    Configura el manejo automático de resize entre la página y el layout.

    Llama a layout.on_resize() en cada cambio de tamaño e inicializa
    con el tamaño actual de la página.

    Args:
        layout: El ResponsiveLayout a conectar.
        page:   La página de Flet.
    """

    def on_page_resize(e):
        layout.on_resize(int(page.width) if page.width else 0)

    page.on_resize = on_page_resize
    # Inicializar con el tamaño actual (puede ser None en el primer frame)
    layout.on_resize(int(page.width) if page.width else 1200)


def create_simple_navbar(
    title: str,
    on_menu_click: Optional[Callable] = None,
    show_menu: bool = True,
) -> ft.Container:
    """
    Crea una barra de navegación superior simple.

    Args:
        title:         Título que se muestra en la barra.
        on_menu_click: Callback al pulsar el botón de menú.
        show_menu:     Si True, muestra el botón de menú (solo si on_menu_click está definido).

    Returns:
        ft.Container con la barra de navegación.
    """
    controls: List[ft.Control] = []

    if show_menu and on_menu_click:
        controls.append(ft.IconButton(icon=ft.Icons.MENU, on_click=on_menu_click))

    controls.append(ft.Text(title, size=20, weight=ft.FontWeight.BOLD))

    return ft.Container(
        content=ft.Row(controls, alignment=ft.MainAxisAlignment.START),
        padding=ft.padding.symmetric(horizontal=10),
        alignment=ft.Alignment.CENTER_LEFT,
    )


def create_simple_sidebar(
    items: List[dict],
    on_click: Optional[Callable[[int], None]] = None,
) -> ft.Container:
    """
    Crea un sidebar con ítems de navegación.

    Args:
        items:    Lista de dicts con claves 'icon' (ft.Icons.*) y 'label' (str).
        on_click: Callback que recibe el índice del ítem pulsado.

    Returns:
        ft.Container con el sidebar.

    Ejemplo::

        items = [
            {"icon": ft.Icons.HOME, "label": "Inicio"},
            {"icon": ft.Icons.SETTINGS, "label": "Ajustes"},
        ]
        sidebar = create_simple_sidebar(items, on_click=lambda idx: print(idx))
    """

    def handle_click(index: int) -> None:
        if on_click:
            on_click(index)

    sidebar_items = [
        ft.ListTile(
            leading=ft.Icon(item["icon"]),
            title=ft.Text(item["label"]),
            on_click=lambda e, idx=i: handle_click(idx),
        )
        for i, item in enumerate(items)
    ]

    return ft.Container(
        content=ft.ListView(controls=sidebar_items, spacing=5),
        padding=10,
    )


def create_footer(text: str = "© 2026") -> ft.Container:
    """
    Crea un pie de página simple con texto centrado.

    Args:
        text: Texto del footer.

    Returns:
        ft.Container con el footer.
    """
    return ft.Container(
        content=ft.Text(text, size=12, color=ft.Colors.GREY_500),
        alignment=ft.Alignment.CENTER,
    )
