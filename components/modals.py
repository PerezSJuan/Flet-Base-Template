import flet as ft

import translations


def alert_modal(title, content, responses=None, on_dismiss=None):
    """It creates an alert modal. The title and content are required, 
    while the responses and on_dismiss are optional. If the responses are not provided, 
    a default dismiss button will be created. The on_dismiss function will be called 
    when the dismiss button is clicked. See this function to learn how to format responses"""
    if responses is None:
        responses = ft.TextButton(
            text=translations.t("dismiss"),
            on_click=lambda e: on_dismiss(e) if on_dismiss else None,
            text_color=ft.Colors.prymary
            
        )
    return ft.AlertDialog(
        title=ft.Text(title),
        content=ft.Text(content),
        actions=[responses],
        open=True,
    )