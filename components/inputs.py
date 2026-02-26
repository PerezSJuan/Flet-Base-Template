import flet as ft
import datetime

def switch(label, on_change=None, value=False, enabled=True):
    """It creates a switch with the specified label and change 
    event handler and the main color of the theme"""
    return ft.Switch(
        label=label,
        on_change=on_change,
        value=value,
        enabled=enabled,
        active_color=ft.Colors.primary,
        inactive_thumb_color=ft.Colors.surface,
    )

def text_autocomplete_input (label, placeholder, on_change=None, value="", enabled=True, suggestions=[]):
    """It creates a text input with autocomplete functionality. 
    The autocomplete options can be easily modified to fit your needs."""
    return ft.TextField(
        label=label,
        hint_text=placeholder,
        on_change=on_change,
        suggestions=suggestions,
        enabled=enabled,
        value=value,
        text_color=ft.Colors.text_color
    )

def checkbox(label, on_change=None, value=False, enabled=True):
    """It creates a checkbox with the specified label and change 
    event handler and the main color of the theme"""
    return ft.Checkbox(
        label=label,
        on_change=on_change,
        value=value,
        enabled=enabled,
        active_color=ft.Colors.primary,
        check_color=ft.Colors.on_primary
    )

def color_picker(label, on_change=None, value="#FFFFFF", enabled=True):
    """It creates a color picker with the specified label and 
    change event handler and the main color of the theme"""
    return ft.ColorPicker(
        label=label,
        on_change=on_change,
        value=value,
        enabled=enabled,
    )

def date_picker(label, on_change=None, value=datetime.date.today(), first_date=datetime.date(1900, 1, 1), last_date=datetime.date.today()):
    """It creates a date picker with the specified label and change 
    event handler and the main color of the theme"""
    return ft.DatePicker(
        label=label,
        on_change=on_change,
        value=value,
        first_date=first_date,
        last_date=last_date
    )


def date_range_picker(label, on_change=None, initial_range=(datetime.date.today(), datetime.date.today()), first_date=datetime.date(1900, 1, 1), last_date=datetime.date.today()):
    """It creates a date range picker with the specified label and change 
    event handler and the main color of the theme"""
    return ft.DatePicker(
        label=label,
        on_change=on_change,
        start_value=initial_range[0],
        end_value=initial_range[1],
        first_date=first_date,
        last_date=last_date
    )


def dropdown(label, options, on_change=None, value=None, enabled=True):
    """It creates a dropdown with the specified label and change 
    event handler and the main color of the theme. The options must be a list of DropdownOption objects."""
    return ft.Dropdown(
        label=label,
        options=options,
        on_change=on_change,
        value=value,
        enabled=enabled,
        text_color=ft.Colors.text_color
    )


def slider (label, on_change=None, value=0, min=0, max=100, step=1, enabled=True):
    """It creates a slider with the specified label and change 
    event handler and the main color of the theme"""
    return ft.Slider(
        label=label,
        on_change=on_change,
        value=value,
        min=min,
        max=max,
        step=step,
        enabled=enabled,
        active_color=ft.Colors.primary,
        inactive_color=ft.Colors.surface
    )