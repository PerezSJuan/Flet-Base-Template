import flet as ft
import flet_datatable2 as fdt

import themes

def datatable(columns, rows, on_row_click=None, width=400, height=300, show_checkbox_column=False):
    """It creates a datatable with the specified columns and rows and the main color of the theme.
    IT IS IMPORTANT TO NOTE THAT THE COLUMNS AND ROWS MUST BE IN THE FORMAT REQUIRED BY FLET_DATATABLE2, AND
    YOU NEED TO INSTALL (AND INCLUDE IN DEPENDENCIES) FLET_DATATABLE2 TO USE THIS COMPONENT. You can check the documentation of FLET_DATATABLE2
      to learn how to format columns and rows. """
    return fdt.DataTable(
        show_checkbox_column=show_checkbox_column,
        expand=True,
        column_spacing=0,
        heading_row_color=ft.Colors.surface,
        horizontal_margin=12,
        sort_ascending=True,
        bottom_margin=10,
        min_width=600,
        on_select_all=lambda e: print("All selected"),
        columns=columns,
        rows=rows,
        width=width,
        height=height,
        bgcolor=ft.Colors.surface,
        border_color=ft.Colors.border_color,
        header_bgcolor=ft.Colors.primary,
        header_text_color=ft.Colors.text_color,
        row_hover_color=ft.Colors.hover_color,
    )


def icon (icon, color=ft.Colors.primary, size=24):
    """It creates an icon with the specified icon, color and size and the main color of the theme"""
    return ft.Icon(
        name=icon,
        color=color,
        size=size
    )


def image(src, width=100, height=100, border_radius=5):
    """It creates an image with the specified source, width and height and the main color of the theme"""
    return ft.Image(
        src=src,
        width=width,
        height=height,
        border_radius=border_radius
    )



def progress_bar(value, width=200, height=10):
    """It creates a progress bar with the specified value, width and height and the main color of the theme"""
    return ft.ProgressBar(
        value=value,
        width=width,
        height=height,
        bgcolor=ft.Colors.surface,
        color=ft.Colors.primary
    )


def loading_indicator(size=50):
    """It creates a loading indicator"""
    return ft.ProgressRing(
        width=size,
        height=size,
        color=ft.Colors.primary
    )