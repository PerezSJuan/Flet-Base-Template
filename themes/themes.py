import flet as ft

# Esquema de colores enriquecido con propiedades adicionales
LIGHT_COLOR_SCHEME = ft.ColorScheme(
    primary="#007BFF",  # Azul principal
    on_primary="#FFFFFF",  # Texto blanco sobre azul
    surface="#F8F9FA",  # Fondo claro
    on_surface="#212529",  # Texto oscuro sobre fondo claro
    text_color="#212529",  # Color de texto principal
    background="#FFFFFF",  # Fondo general
    on_background="#000000",  # Texto sobre fondo general
    filled_button_text_color="#FFFFFF",  # Color del texto en botones llenos
    red_color="#DC3545",  # Color para acciones de eliminación o advertencia
)

DARK_COLOR_SCHEME = ft.ColorScheme(
    primary="#6C757D",  # Gris principal
    on_primary="#FFFFFF",  # Texto blanco sobre gris
    surface="#343A40",  # Fondo oscuro
    on_surface="#E9ECEF",  # Texto claro sobre fondo oscuro
    text_color="#E9ECEF",  # Color de texto principal
    background="#1E1E1E",  # Fondo general
    on_background="#FFFFFF",  # Texto sobre fondo general
    filled_button_text_color="#000000",  # Color del texto en botones llenos
    red_color="#DC3545",  # Color para acciones de eliminación o advertencia
)

# Temas enriquecidos
LIGHT_THEME = ft.Theme(color_scheme=LIGHT_COLOR_SCHEME, use_material3=True)
DARK_THEME = ft.Theme(color_scheme=DARK_COLOR_SCHEME, use_material3=True)

async def awake_theme(page: ft.Page) -> str:
    """
    Inicializa el tema de la página basándose en el almacenamiento local o el sistema.
    """
    # Obtener el tema guardado
    stored_theme = await page.shared_preferences.get("theme")

    if not stored_theme:
        # Si no hay nada guardado, usamos "light" por defecto y lo guardamos
        stored_theme = "light"
        await page.shared_preferences.set("theme", "light")

    # Aplicar el tema a la página
    if stored_theme == "dark":
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.LIGHT

    # Asignar los objetos de tema
    page.theme = LIGHT_THEME
    page.dark_theme = DARK_THEME

    page.update()
    return stored_theme


async def toggle_theme(page: ft.Page):
    """
    Cambia entre tema claro y oscuro y persiste la elección.
    """
    if page.theme_mode == ft.ThemeMode.DARK:
        page.theme_mode = ft.ThemeMode.LIGHT
        await page.shared_preferences.set("theme", "light")
    else:
        page.theme_mode = ft.ThemeMode.DARK
        await page.shared_preferences.set("theme", "dark")

    page.update()


def get_theme_colors(page: ft.Page) -> ft.ColorScheme:
    """
    Retorna el esquema de colores activo actualmente en la página.
    """
    if page.theme_mode == ft.ThemeMode.DARK:
        return DARK_COLOR_SCHEME
    return LIGHT_COLOR_SCHEME

def apply_theme(page: ft.Page, theme_mode: str = "light"):
    """
    Aplica el tema especificado a la página.

    Args:
        page (ft.Page): Página de Flet.
        theme_mode (str): Modo de tema, "light" o "dark".
    """
    if theme_mode == "dark":
        page.theme_mode = ft.ThemeMode.DARK
        page.theme = DARK_THEME
    else:
        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = LIGHT_THEME

    page.update()
