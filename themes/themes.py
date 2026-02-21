from typing import Dict
import flet as ft


LIGHT_THEME: Dict[str, str] = {
    "primary": "#1976D2",
    "on_primary": "#FFFFFF",
    "primary_container": "#BBDEFB",
    "on_primary_container": "#0D47A1",
    "secondary": "#9C27B0",
    "on_secondary": "#FFFFFF",
    "secondary_container": "#E1BEE7",
    "on_secondary_container": "#4A148C",
    "tertiary": "#FF5722",
    "on_tertiary": "#FFFFFF",
    "background": "#FFFFFF",
    "on_background": "#000000",
    "surface": "#FFFFFF",
    "on_surface": "#000000",
    "surface_variant": "#F5F5F5",
    "error": "#B00020",
    "on_error": "#FFFFFF",
    "success": "#2E7D32",
    "info": "#0288D1",
    "warning": "#F9A825",
    "outline": "#BDBDBD",
    "shadow": "rgba(0,0,0,0.2)",
    "scrim": "rgba(0,0,0,0.6)",
    "inverse_surface": "#121212",
    "inverse_on_surface": "#FFFFFF",
}


DARK_THEME: Dict[str, str] = {
    "primary": "#90CAF9",
    "on_primary": "#0D47A1",
    "primary_container": "#1565C0",
    "on_primary_container": "#E3F2FD",
    "secondary": "#CE93D8",
    "on_secondary": "#4A148C",
    "secondary_container": "#6A1B9A",
    "on_secondary_container": "#F3E5F5",
    "tertiary": "#FFAB91",
    "on_tertiary": "#000000",
    "background": "#121212",
    "on_background": "#FFFFFF",
    "surface": "#1E1E1E",
    "on_surface": "#FFFFFF",
    "surface_variant": "#2C2C2C",
    "error": "#CF6679",
    "on_error": "#000000",
    "success": "#81C784",
    "info": "#64B5F6",
    "warning": "#FFD54F",
    "outline": "#373737",
    "shadow": "rgba(0,0,0,0.7)",
    "scrim": "rgba(0,0,0,0.8)",
    "inverse_surface": "#FFFFFF",
    "inverse_on_surface": "#000000",
}


def awake_theme(page: ft.page) -> str:
    stored_theme = page.client_storage.get("theme")
    if not stored_theme:
        if page.ThemeMode.SYSTEM == ft.ThemeMode.DARK_THEME:
            stored_theme = "dark"
            page.client_storage.set("theme", "dark")
            page.theme_mode = ft.ThemeMode.DARK_THEME
        elif page.ThemeMode.SYSTEM == ft.ThemeMode.LIGHT_THEME:
            stored_theme = "light"
            page.client_storage.set("theme", "light")
            page.theme_mode = ft.ThemeMode.LIGHT_THEME
    if stored_theme:
        if stored_theme == "dark":
            page.theme_mode = ft.ThemeMode.DARK_THEME
        elif stored_theme == "light":
            page.theme_mode = ft.ThemeMode.LIGHT_THEME
    return stored_theme


theme = awake_theme()


def get_theme_colors(mode: str = theme) -> Dict[str, str]:
    if mode.lower() == "light":
        return LIGHT_THEME
    elif mode.lower() == "dark":
        return DARK_THEME
    else:
        print("Modo de tema desconocido: usar 'light' o 'dark'.")
