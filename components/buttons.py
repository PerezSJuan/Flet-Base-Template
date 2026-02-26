import flet as ft

def filled_btn(text, icon=None, on_click=None, enabled=True):
    """It creates a filled button with the specified text and click 
    event handler and the main color of the theme"""
    return ft.FilledButton(
        text=text,
        icon=icon,
        on_click=on_click,
        bgcolor=ft.Colors.primary,
        enabled=enabled,
        text_color=ft.Colors.filled_button_text_color
    )


def icon_filled_btn(icon, on_click=None, enabled=True):
    """It creates a filled button with the specified icon and click 
    event handler and the main color of the theme"""
    return ft.FilledIconButton(
        icon=icon,
        on_click=on_click,
        bgcolor=ft.Colors.primary,
        enabled=enabled,
        text_color=ft.Colors.filled_button_text_color
    )

def icon_btn (icon, on_click=None, enabled=True):
    """It creates a empty button with the specified icon and click 
    event handler and the main color of the theme"""
    return ft.IconButton(
        icon=icon,
        on_click=on_click,
        enabled=enabled,
        icon_color=ft.Colors.primary
    )

def text_btn(text, icon=None, on_click=None, enabled=True):
    """It creates a empty (no bg) button with the specified text 
    and the option of an icon and click event handler and the main
    color of the theme"""
    return ft.TextButton(
        text=text,
        icon=icon,
        on_click=on_click,
        enabled=enabled,
        text_color=ft.Colors.text_color
    )

def btn(text, icon=None, on_click=None, enabled=True):
    """It creates a empty button with the specified text and the
      option of an icon and click event handler and the main color 
      of the theme"""
    return ft.FilledButton(
        text=text,
        icon=icon,
        on_click=on_click,
        bgcolor=ft.Colors.background,
        enabled=enabled,
        text_color=ft.Colors.text_color
    )