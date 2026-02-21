"""
screen_system.py
================
Sistema de enrutamiento y pantallas para Flet.

Clases:
    Screen: Clase base para todas las pantallas de la aplicación.
    ScreenRouter: Gestor de rutas que renderiza la pantalla activa y maneja transiciones.
"""

import flet as ft
from typing import Callable, Dict, List, Optional, Type


class Screen:
    """
    Clase base para construir pantallas.
    """

    route: str = "/"

    def __init__(self, page: ft.Page):
        self.page = page

    def build(self) -> ft.Control:
        """
        Retorna el control principal (el contenido) de la pantalla.
        """
        return ft.Container()

    def get_appbar_actions(self) -> List[ft.Control]:
        """
        Retorna una lista de controles a inyectar en la AppBar u otra barra externa.
        """
        return []

    def get_fab(self) -> Optional[ft.Control]:
        """
        Retorna un FloatingActionButton si la pantalla lo requiere.
        """
        return None

    def on_load(self) -> None:
        """
        Se llama cuando la pantalla se vuelve activa.
        """
        pass

    def on_unload(self) -> None:
        """
        Se llama antes de que la pantalla actual sea destruida/reemplazada.
        """
        pass


class ScreenRouter:
    """
    Enrutador para manejar el cambio de pantallas (Screen) dentro de un contenedor.
    Ideal para integrarse con ResponsiveLayout u otros layouts base.
    """

    def __init__(
        self,
        page: ft.Page,
        on_route_change_complete: Optional[Callable[[Screen], None]] = None,
        animate_transitions: bool = True,
        transition_duration_ms: int = 300,
    ):
        self.page = page
        self.routes: Dict[str, Type[Screen]] = {}
        self.current_screen: Optional[Screen] = None
        self.on_route_change_complete = on_route_change_complete

        self.animate_transitions = animate_transitions
        self.transition_duration_ms = transition_duration_ms

        # Contenedor padre donde se renderizará el contenido de las pantallas
        self.content_container = ft.Container(expand=True)

        if self.animate_transitions:
            self.content_container.animate_opacity = ft.Animation(
                duration=self.transition_duration_ms, curve=ft.AnimationCurve.EASE_IN
            )
            self.content_container.opacity = 1.0

        # Conectar eventos de Flet
        self.page.on_route_change = self._handle_route_change
        self.page.on_view_pop = self._handle_view_pop

    def register_routes(self, screens: List[Type[Screen]]) -> None:
        """
        Registra una lista de clases que hereden de Screen.
        """
        for screen_class in screens:
            self.routes[screen_class.route] = screen_class

    def register_route(self, screen_class: Type[Screen]) -> None:
        """
        Registra una única clase Screen.
        """
        self.routes[screen_class.route] = screen_class

    def go(self, route: str) -> None:
        """
        Navega a una nueva ruta.
        """
        self.page.go(route)

    def _handle_route_change(self, e: ft.RouteChangeEvent) -> None:
        """
        Intercepta el cambio de ruta de la página y cambia el contenido del contenedor principal.
        """
        route = e.route

        # Limpiar parámetros extra en la ruta web (ej. /home?param=1)
        base_route = route.split("?")[0] if "?" in route else route

        screen_class = self.routes.get(base_route)
        if not screen_class:
            return  # Ruta no encontrada

        self._transition_to_screen(screen_class)

    def _transition_to_screen(self, screen_class: Type[Screen]) -> None:
        """
        Realiza la transición visual y lógica a la nueva pantalla.
        """

        def render_new_screen():
            # Desmontar pantalla anterior
            if self.current_screen:
                self.current_screen.on_unload()

            # Inicializar y montar nueva pantalla
            self.current_screen = screen_class(self.page)
            new_content = self.current_screen.build()

            self.content_container.content = new_content
            self.current_screen.on_load()

            if self.animate_transitions:
                self.content_container.opacity = 1.0

            self.content_container.update()

            # Avisar que la pantalla cambió (útil para inyectar botones en el top bar)
            if self.on_route_change_complete:
                self.on_route_change_complete(self.current_screen)

        if self.animate_transitions and self.content_container.content is not None:
            # Fade out
            self.content_container.opacity = 0.0
            self.content_container.update()

            # Esperar a que termine la animación antes de renderizar la nueva
            import threading

            threading.Timer(
                self.transition_duration_ms / 1000.0, render_new_screen
            ).start()
        else:
            # Sin animación / primera carga
            render_new_screen()

    def _handle_view_pop(self, e: ft.ViewPopEvent) -> None:
        """
        Maneja el evento de ir atrás en el historial.
        Para un sistema de una sola vista dinámica, sacamos la vista superior si la hay.
        """
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)
