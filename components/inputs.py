import flet as ft

def Switch(label, on_change=None, value=False, enabled=True):
    """It creates a switch with the specified label and change event handler and the main color of the theme"""
    return ft.Switch(
        label=label,
        on_change=on_change,
        value=value,
        enabled=enabled,
        active_color=ft.Colors.primary,
        inactive_thumb_color=ft.Colors.surface,
    )