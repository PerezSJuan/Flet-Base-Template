"""
ejemplo_dashboard.py
====================
Ejemplo completo: dashboard con top bar, sidebar izquierdo y footer.

Demuestra:
    - Layout con 3 barras simultáneas
    - Navegación entre vistas sin reconstruir el layout
    - Toggle de sidebar animado con botón de menú
    - Tarjetas de métricas
    - Uso completo de helpers

NOTA: Las vistas NO deben configurar scroll propio — el layout ya lo gestiona.
"""

import flet as ft
from layout_system import LayoutBuilder
from layout_helpers import (
    create_simple_navbar,
    create_simple_sidebar,
    create_footer,
    setup_responsive_layout,
)

# ── Estado global (evita closures circulares) ──────────────────────────────────
_state: dict = {
    "layout": None,
    "content_area": None,
    "switcher": None,
}


def _metric_card(label: str, value: str, icon, color: str) -> ft.Container:
    """Tarjeta de métrica reutilizable."""
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(icon, color=color, size=28),
                        ft.Text(label, size=13, color=ft.Colors.GREY_600),
                    ],
                    spacing=8,
                ),
                ft.Text(value, size=28, weight=ft.FontWeight.BOLD),
            ],
            spacing=6,
        ),
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        border=ft.border.all(1, ft.Colors.GREY_200),
        expand=True,
    )


# ── Vistas ─────────────────────────────────────────────────────────────────────
# IMPORTANTE: no usar scroll= en las vistas; el layout lo gestiona.


def _view_inicio() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Dashboard", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Resumen de actividad", color=ft.Colors.GREY_600),
            ft.Divider(height=24),
            ft.Row(
                controls=[
                    _metric_card(
                        "Usuarios", "1,248", ft.Icons.PEOPLE, ft.Colors.BLUE_600
                    ),
                    _metric_card(
                        "Ingresos", "$8,430", ft.Icons.ATTACH_MONEY, ft.Colors.GREEN_600
                    ),
                    _metric_card(
                        "Pedidos", "342", ft.Icons.SHOPPING_CART, ft.Colors.ORANGE_600
                    ),
                    _metric_card(
                        "Tendencia", "+12%", ft.Icons.TRENDING_UP, ft.Colors.PURPLE_600
                    ),
                ],
                wrap=True,
                spacing=16,
            ),
            ft.Divider(height=24),
            ft.Text("Actividad reciente", size=18, weight=ft.FontWeight.W_600),
            ft.Column(
                controls=[
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.CIRCLE, color=ft.Colors.GREEN_400, size=12
                        ),
                        title=ft.Text("Nuevo usuario registrado"),
                        subtitle=ft.Text("Hace 5 minutos"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.CIRCLE, color=ft.Colors.BLUE_400, size=12
                        ),
                        title=ft.Text("Pedido #4521 completado"),
                        subtitle=ft.Text("Hace 23 minutos"),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(
                            ft.Icons.CIRCLE, color=ft.Colors.ORANGE_400, size=12
                        ),
                        title=ft.Text("Alerta de inventario bajo"),
                        subtitle=ft.Text("Hace 1 hora"),
                    ),
                ],
                spacing=0,
            ),
        ],
        spacing=8,
    )


def _view_usuarios() -> ft.Control:
    usuarios = [
        ("Ana García", "ana@example.com", "Admin"),
        ("Carlos López", "carlos@example.com", "Editor"),
        ("María Torres", "maria@example.com", "Viewer"),
        ("Luis Martín", "luis@example.com", "Editor"),
        ("Sofía Ruiz", "sofia@example.com", "Admin"),
    ]
    rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(nombre)),
                ft.DataCell(ft.Text(email)),
                ft.DataCell(
                    ft.Container(
                        content=ft.Text(rol, size=12),
                        bgcolor=ft.Colors.BLUE_100,
                        padding=ft.padding.symmetric(horizontal=8, vertical=4),
                        border_radius=12,
                    )
                ),
            ]
        )
        for nombre, email, rol in usuarios
    ]
    return ft.Column(
        controls=[
            ft.Text("Usuarios", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Gestión de usuarios del sistema", color=ft.Colors.GREY_600),
            ft.Divider(height=24),
            ft.Row(
                controls=[
                    ft.TextField(
                        hint_text="Buscar usuario...",
                        expand=True,
                        prefix_icon=ft.Icons.SEARCH,
                    ),
                    ft.ElevatedButton("Nuevo usuario", icon=ft.Icons.PEOPLE),
                ],
                spacing=12,
            ),
            ft.Divider(height=12),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Nombre", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("Email", weight=ft.FontWeight.BOLD)),
                    ft.DataColumn(ft.Text("Rol", weight=ft.FontWeight.BOLD)),
                ],
                rows=rows,
                border=ft.border.all(1, ft.Colors.GREY_200),
                border_radius=8,
            ),
        ],
        spacing=8,
    )


def _view_configuracion() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Configuración", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Ajustes de la aplicación", color=ft.Colors.GREY_600),
            ft.Divider(height=24),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("General", size=16, weight=ft.FontWeight.W_600),
                        ft.Divider(),
                        ft.ListTile(
                            title=ft.Text("Notificaciones"),
                            subtitle=ft.Text("Recibir alertas del sistema"),
                            trailing=ft.Switch(value=True),
                        ),
                        ft.ListTile(
                            title=ft.Text("Modo oscuro"),
                            subtitle=ft.Text("Cambiar apariencia de la interfaz"),
                            trailing=ft.Switch(value=False),
                        ),
                        ft.ListTile(
                            title=ft.Text("Idioma"),
                            subtitle=ft.Text("Español"),
                            trailing=ft.Icon(ft.Icons.STAR),
                        ),
                    ],
                ),
                padding=16,
                bgcolor=ft.Colors.WHITE,
                border_radius=12,
                border=ft.border.all(1, ft.Colors.GREY_200),
            ),
        ],
        spacing=8,
    )


def _view_analiticas() -> ft.Control:
    return ft.Column(
        controls=[
            ft.Text("Analíticas", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Datos de rendimiento del sistema", color=ft.Colors.GREY_600),
            ft.Divider(height=24),
            ft.Row(
                controls=[
                    _metric_card(
                        "Sesiones hoy", "587", ft.Icons.ASSESSMENT, ft.Colors.TEAL_600
                    ),
                    _metric_card(
                        "Tasa conversión",
                        "3.2%",
                        ft.Icons.TRENDING_UP,
                        ft.Colors.INDIGO_600,
                    ),
                ],
                wrap=True,
                spacing=16,
            ),
            ft.Divider(height=16),
            ft.Text(
                "Próximamente: gráficos de tendencias",
                italic=True,
                color=ft.Colors.GREY_500,
            ),
        ],
        spacing=8,
    )


# ── App principal ──────────────────────────────────────────────────────────────

_VISTAS = [_view_inicio, _view_usuarios, _view_configuracion, _view_analiticas]


def main(page: ft.Page):
    page.title = "Dashboard Pro - Flet Layout"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    # Área de contenido dinámica: no usar expand=True aquí, el layout lo gestiona
    _state["switcher"] = ft.AnimatedSwitcher(
        content=_view_inicio(),
        duration=350,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
    )
    _state["content_area"] = ft.Container(
        content=_state["switcher"],
        padding=28,
    )

    # ── Callbacks ──────────────────────────────────────────────────────────────
    def change_view(index: int) -> None:
        _state["switcher"].content = _VISTAS[index]()
        _state["switcher"].update()

    def handle_menu(e=None) -> None:
        if _state["layout"]:
            _state["layout"].toggle_left_sidebar()

    # ── Componentes ────────────────────────────────────────────────────────────
    navbar = create_simple_navbar(
        "Dashboard Pro",
        on_menu_click=handle_menu,
        show_menu=True,
    )

    sidebar_items = [
        {"icon": ft.Icons.DASHBOARD, "label": "Dashboard"},
        {"icon": ft.Icons.PEOPLE, "label": "Usuarios"},
        {"icon": ft.Icons.SETTINGS, "label": "Configuración"},
        {"icon": ft.Icons.ASSESSMENT, "label": "Analíticas"},
    ]
    sidebar = create_simple_sidebar(sidebar_items, on_click=change_view)
    footer = create_footer("Dashboard Pro © 2026")

    # ── Construcción del layout ────────────────────────────────────────────────
    _state["layout"] = (
        LayoutBuilder()
        .with_content(_state["content_area"])
        .with_top_bar(navbar, height=64, bgcolor=ft.Colors.INDIGO_700)
        .with_left_bar(sidebar, width=260, bgcolor=ft.Colors.GREY_50)
        .with_bottom_bar(footer, height=40)
        .with_responsive_config(
            breakpoint_mobile=600,
            breakpoint_tablet=1024,
            collapse_sidebars_on_mobile=True,
            collapse_sidebars_on_tablet=True,
        )
        .with_transitions(
            duration_ms=650,
            curve=ft.AnimationCurve.EASE_IN_OUT,
            fade_sidebars=True,
        )
        .build()
    )

    page.add(_state["layout"])
    setup_responsive_layout(_state["layout"], page)


if __name__ == "__main__":
    ft.app(target=main)
