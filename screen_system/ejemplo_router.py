import flet as ft
from layout.layout_system import LayoutBuilder
from screen_system.screen_system import Screen, ScreenRouter


# 1. Definimos nuestras pantallas personalizadas
class HomeScreen(Screen):
    route = "/"

    def build(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Bienvenido al Inicio", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Aquí no hay acciones especiales en el Top Bar."),
                    ft.ElevatedButton(
                        "Ir a Preferencias",
                        on_click=lambda _: self.page.go("/settings"),
                    ),
                ]
            ),
            padding=20,
        )


class SettingsScreen(Screen):
    route = "/settings"

    def build(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Preferencias", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "¡Mira arriba! Esta pantalla inyecta un botón en el Top Bar."
                    ),
                    ft.ElevatedButton(
                        "Volver al Inicio", on_click=lambda _: self.page.go("/")
                    ),
                ]
            ),
            padding=20,
        )

    # Inyectamos acciones dinámicas al layout externo
    def get_appbar_actions(self) -> list[ft.Control]:
        def save_clicked(e):
            print("Configuración guardada.")

        return [
            ft.IconButton(
                icon=ft.icons.SAVE,
                tooltip="Guardar preferencias",
                on_click=save_clicked,
            )
        ]


def main(page: ft.Page):
    page.title = "Screen Router Ejemplo"
    page.theme_mode = ft.ThemeMode.LIGHT

    # 1. Título fijo en el AppBar
    appbar_title = ft.Text("Mi App Responsiva", size=20, weight=ft.FontWeight.W_500)

    # Este Row contendrá las acciones inyectadas por la pantalla activa
    appbar_actions_container = ft.Row(spacing=5)

    # El AppBar real (o un Top Bar manual)
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.Row([ft.Icon(ft.icons.MENU), appbar_title]),
                appbar_actions_container,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # Sidebar básico
    left_bar = ft.Container(
        content=ft.Column(
            [
                ft.TextButton(
                    "Inicio", icon=ft.icons.HOME, on_click=lambda _: page.go("/")
                ),
                ft.TextButton(
                    "Opciones",
                    icon=ft.icons.SETTINGS,
                    on_click=lambda _: page.go("/settings"),
                ),
            ]
        ),
        padding=10,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # 2. Callback del router: Se ejecuta cada vez que cambiamos de pantalla
    def on_screen_changed(screen: Screen):
        # Actualizamos las acciones del Top Bar con las que la pantalla pide
        appbar_actions_container.controls = screen.get_appbar_actions()
        page.update()

    # 3. Inicializamos el Router
    router = ScreenRouter(
        page=page,
        on_route_change_complete=on_screen_changed,
        animate_transitions=True,  # Animación de fade activada
        transition_duration_ms=400,
    )

    # Registramos las pantallas (rutas)
    router.register_routes([HomeScreen, SettingsScreen])

    # 4. Construimos el ResponsiveLayout usando el contenedor del router como contenido principal
    layout = (
        LayoutBuilder()
        .with_top_bar(top_bar, height=60)
        .with_left_bar(left_bar, width=200)
        .with_content(router.content_container)  # <- Aquí conectamos el enrutador
        .build()
    )

    page.add(layout)

    # Iniciamos en la ruta principal
    page.go("/")


ft.app(target=main)
