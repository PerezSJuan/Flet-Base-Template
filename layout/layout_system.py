"""
layout_system.py
================
Sistema de layouts responsive profesional para Flet.

Clases:
    ResponsiveLayout: Layout principal con soporte para barras top/bottom/left/right.
    LayoutBuilder: Builder fluido para construir ResponsiveLayout fácilmente.
"""

import flet as ft
from typing import Optional


class ResponsiveLayout(ft.Container):
    """
    Layout responsive para aplicaciones Flet con soporte para múltiples barras.

    Estructura interna:
        Container (ResponsiveLayout)
        └── Column (expand=True, spacing=0)
            ├── Container (top_bar)       [opcional, altura fija]
            ├── Row (expand=True)
            │   ├── Container (left_bar)  [opcional, ancho fijo, colapsable]
            │   ├── Container (content)   [expand=True]
            │   └── Container (right_bar) [opcional, ancho fijo, colapsable]
            └── Container (bottom_bar)    [opcional, altura fija]
    """

    def __init__(
        self,
        content: ft.Control,
        top_bar: Optional[ft.Control] = None,
        bottom_bar: Optional[ft.Control] = None,
        left_bar: Optional[ft.Control] = None,
        right_bar: Optional[ft.Control] = None,
        top_bar_height: int = 60,
        bottom_bar_height: int = 60,
        left_bar_width: int = 250,
        right_bar_width: int = 250,
        top_bar_bgcolor: Optional[str] = None,
        bottom_bar_bgcolor: Optional[str] = None,
        left_bar_bgcolor: Optional[str] = None,
        right_bar_bgcolor: Optional[str] = None,
        breakpoint_mobile: int = 600,
        breakpoint_tablet: int = 1024,
        collapse_sidebars_on_mobile: bool = True,
        collapse_sidebars_on_tablet: bool = False,
        left_bar_collapsible: bool = True,
        right_bar_collapsible: bool = True,
        animate_transitions: bool = True,
        transition_duration_ms: int = 300,
        transition_curve: ft.AnimationCurve = ft.AnimationCurve.DECELERATE,
        fade_sidebars: bool = False,
    ):
        super().__init__(expand=True)

        # Controles de las barras
        self.main_content = content
        self.top_bar_control = top_bar
        self.bottom_bar_control = bottom_bar
        self.left_bar_control = left_bar
        self.right_bar_control = right_bar

        # Configuración de responsividad
        self.breakpoint_mobile = breakpoint_mobile
        self.breakpoint_tablet = breakpoint_tablet
        self.collapse_sidebars_on_mobile = collapse_sidebars_on_mobile
        self.collapse_sidebars_on_tablet = collapse_sidebars_on_tablet
        self.left_bar_collapsible = left_bar_collapsible
        self.right_bar_collapsible = right_bar_collapsible

        # Animación para transiciones suaves
        self._fade_sidebars = fade_sidebars
        anim = (
            ft.Animation(transition_duration_ms, transition_curve)
            if animate_transitions
            else None
        )

        # --- Contenedores de barras ---

        self.top_container = ft.Container(
            content=self.top_bar_control,
            height=top_bar_height,
            bgcolor=top_bar_bgcolor,
            visible=self.top_bar_control is not None,
        )

        self.bottom_container = ft.Container(
            content=self.bottom_bar_control,
            height=bottom_bar_height,
            bgcolor=bottom_bar_bgcolor,
            visible=self.bottom_bar_control is not None,
        )

        # Guardamos el ancho original para restaurarlo al abrir
        self._left_bar_width = left_bar_width
        self._right_bar_width = right_bar_width
        self._left_open = self.left_bar_control is not None
        self._right_open = self.right_bar_control is not None

        # Contenedores internos para animación de deslizamiento (slide) y fade
        self.left_inner = ft.Container(
            content=self.left_bar_control,
            animate_offset=anim,
            animate_opacity=anim,
            offset=ft.Offset(0, 0) if self._left_open else ft.Offset(-0.1, 0),
            opacity=1.0 if self._left_open else 0.0,
            width=left_bar_width,  # Mantener el ancho real dentro
        )

        self.right_inner = ft.Container(
            content=self.right_bar_control,
            animate_offset=anim,
            animate_opacity=anim,
            offset=ft.Offset(0, 0) if self._right_open else ft.Offset(0.1, 0),
            opacity=1.0 if self._right_open else 0.0,
            width=right_bar_width,
        )

        self.left_container = ft.Container(
            content=self.left_inner,
            width=left_bar_width if self._left_open else 0,
            bgcolor=left_bar_bgcolor,
            animate_size=anim,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            visible=self.left_bar_control is not None,
        )

        self.right_container = ft.Container(
            content=self.right_inner,
            width=right_bar_width if self._right_open else 0,
            bgcolor=right_bar_bgcolor,
            animate_size=anim,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            visible=self.right_bar_control is not None,
        )

        self.center_content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[self.main_content],
                        scroll=ft.ScrollMode.AUTO,  # barra horizontal si desborda
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    )
                ],
                scroll=ft.ScrollMode.AUTO,  # barra vertical si desborda
                expand=True,
            ),
            expand=True,
        )

        # --- Estado de dispositivo ---
        self._is_mobile = False
        self._is_tablet = False
        self._is_desktop = True

        # --- Estructura del layout ---
        self.content = ft.Column(
            controls=[
                self.top_container,
                ft.Row(
                    controls=[
                        self.left_container,
                        self.center_content,
                        self.right_container,
                    ],
                    expand=True,
                    spacing=0,
                ),
                self.bottom_container,
            ],
            spacing=0,
        )

    # --- Propiedades de dispositivo ---

    @property
    def is_mobile(self) -> bool:
        """True si el ancho actual es menor que breakpoint_mobile."""
        return self._is_mobile

    @property
    def is_tablet(self) -> bool:
        """True si el ancho actual está entre breakpoint_mobile y breakpoint_tablet."""
        return self._is_tablet

    @property
    def is_desktop(self) -> bool:
        """True si el ancho actual es mayor o igual que breakpoint_tablet."""
        return self._is_desktop

    # --- Métodos públicos ---

    def toggle_left_sidebar(self) -> None:
        """Alterna la barra lateral izquierda con animación de deslizamiento y fade."""
        if not self.left_bar_control or not self.left_bar_collapsible:
            return
        self._left_open = not self._left_open
        self.left_container.width = self._left_bar_width if self._left_open else 0
        self.left_inner.offset = (
            ft.Offset(0, 0) if self._left_open else ft.Offset(-0.2, 0)
        )
        self.left_inner.opacity = 1.0 if self._left_open else 0.0
        self.update()

    def toggle_right_sidebar(self) -> None:
        """Alterna la barra lateral derecha con animación de deslizamiento y fade."""
        if not self.right_bar_control or not self.right_bar_collapsible:
            return
        self._right_open = not self._right_open
        self.right_container.width = self._right_bar_width if self._right_open else 0
        self.right_inner.offset = (
            ft.Offset(0, 0) if self._right_open else ft.Offset(0.2, 0)
        )
        self.right_inner.opacity = 1.0 if self._right_open else 0.0
        self.update()

    def on_resize(self, width: int) -> None:
        """
        Actualiza el estado del layout al cambiar el ancho de la ventana.

        Args:
            width: Ancho actual de la página en píxeles.
        """
        if width is None:
            return

        # Actualizar estado de dispositivo
        self._is_mobile = width < self.breakpoint_mobile
        self._is_tablet = self.breakpoint_mobile <= width < self.breakpoint_tablet
        self._is_desktop = width >= self.breakpoint_tablet

        # Colapsar/mostrar sidebars según configuración
        if self.left_bar_control:
            should_collapse = (
                self._is_mobile and self.collapse_sidebars_on_mobile
            ) or (self._is_tablet and self.collapse_sidebars_on_tablet)
            self._left_open = not should_collapse
            self.left_container.width = self._left_bar_width if self._left_open else 0
            self.left_inner.offset = (
                ft.Offset(0, 0) if self._left_open else ft.Offset(-0.2, 0)
            )
            self.left_inner.opacity = 1.0 if self._left_open else 0.0

        if self.right_bar_control:
            should_collapse = (
                self._is_mobile and self.collapse_sidebars_on_mobile
            ) or (self._is_tablet and self.collapse_sidebars_on_tablet)
            self._right_open = not should_collapse
            self.right_container.width = (
                self._right_bar_width if self._right_open else 0
            )
            self.right_inner.offset = (
                ft.Offset(0, 0) if self._right_open else ft.Offset(0.2, 0)
            )
            self.right_inner.opacity = 1.0 if self._right_open else 0.0

        self.update()


class LayoutBuilder:
    """
    Builder fluido para construir un ResponsiveLayout de forma legible.

    Ejemplo::

        layout = (
            LayoutBuilder()
            .with_content(mi_contenido)
            .with_top_bar(navbar, height=60)
            .with_left_bar(sidebar, width=250)
            .build()
        )
    """

    def __init__(self):
        self._params: dict = {}

    def with_content(self, content: ft.Control) -> "LayoutBuilder":
        """Establece el contenido principal (obligatorio)."""
        self._params["content"] = content
        return self

    def with_top_bar(
        self,
        bar: ft.Control,
        height: int = 60,
        bgcolor: Optional[str] = None,
    ) -> "LayoutBuilder":
        """Configura la barra superior."""
        self._params["top_bar"] = bar
        self._params["top_bar_height"] = height
        self._params["top_bar_bgcolor"] = bgcolor
        return self

    def with_bottom_bar(
        self,
        bar: ft.Control,
        height: int = 60,
        bgcolor: Optional[str] = None,
    ) -> "LayoutBuilder":
        """Configura la barra inferior."""
        self._params["bottom_bar"] = bar
        self._params["bottom_bar_height"] = height
        self._params["bottom_bar_bgcolor"] = bgcolor
        return self

    def with_left_bar(
        self,
        bar: ft.Control,
        width: int = 250,
        bgcolor: Optional[str] = None,
        collapsible: bool = True,
    ) -> "LayoutBuilder":
        """Configura la barra lateral izquierda."""
        self._params["left_bar"] = bar
        self._params["left_bar_width"] = width
        self._params["left_bar_bgcolor"] = bgcolor
        self._params["left_bar_collapsible"] = collapsible
        return self

    def with_right_bar(
        self,
        bar: ft.Control,
        width: int = 250,
        bgcolor: Optional[str] = None,
        collapsible: bool = True,
    ) -> "LayoutBuilder":
        """Configura la barra lateral derecha."""
        self._params["right_bar"] = bar
        self._params["right_bar_width"] = width
        self._params["right_bar_bgcolor"] = bgcolor
        self._params["right_bar_collapsible"] = collapsible
        return self

    def with_responsive_config(
        self,
        breakpoint_mobile: int = 600,
        breakpoint_tablet: int = 1024,
        collapse_sidebars_on_mobile: bool = True,
        collapse_sidebars_on_tablet: bool = False,
    ) -> "LayoutBuilder":
        """Configura los breakpoints y comportamiento responsive."""
        self._params["breakpoint_mobile"] = breakpoint_mobile
        self._params["breakpoint_tablet"] = breakpoint_tablet
        self._params["collapse_sidebars_on_mobile"] = collapse_sidebars_on_mobile
        self._params["collapse_sidebars_on_tablet"] = collapse_sidebars_on_tablet
        return self

    def with_transitions(
        self,
        animate: bool = True,
        duration_ms: int = 300,
        curve: ft.AnimationCurve = ft.AnimationCurve.DECELERATE,
        fade_sidebars: bool = False,
    ) -> "LayoutBuilder":
        """Configura animación global (duración/curva) y fade opcional de sidebars."""
        self._params["animate_transitions"] = animate
        self._params["transition_duration_ms"] = duration_ms
        self._params["transition_curve"] = curve
        self._params["fade_sidebars"] = fade_sidebars
        return self

    def build(self) -> ResponsiveLayout:
        """Construye y retorna el ResponsiveLayout con la configuración definida."""
        if "content" not in self._params:
            raise ValueError(
                "El contenido principal es obligatorio. Usa .with_content(control) antes de .build()."
            )
        return ResponsiveLayout(**self._params)
