import unittest
from unittest.mock import Mock, MagicMock
import flet as ft
from screen_system.screen_system import Screen, ScreenRouter


class DummyScreen1(Screen):
    route = "/one"

    def __init__(self, page):
        super().__init__(page)
        self.load_called = False
        self.unload_called = False

    def build(self):
        return ft.Text("Screen 1")

    def get_appbar_actions(self):
        return [ft.Text("Action 1")]

    def on_load(self):
        self.load_called = True

    def on_unload(self):
        self.unload_called = True


class DummyScreen2(Screen):
    route = "/two"

    def build(self):
        return ft.Text("Screen 2")


class TestScreenSystem(unittest.TestCase):
    def setUp(self):
        self.page = MagicMock(spec=ft.Page)
        self.callback = Mock()
        # Deshabilitamos la animación real para los tests para que sean síncronos
        self.router = ScreenRouter(
            self.page, on_route_change_complete=self.callback, animate_transitions=False
        )
        # Mockear el método update() del container para que Flet no se queje
        # de que el control no está añadido a la página
        self.router.content_container.update = Mock()
        self.router.register_routes([DummyScreen1, DummyScreen2])

    def test_routing(self):
        # Simulamos cambio de ruta a /one
        route_event = Mock()
        route_event.route = "/one"
        self.router._handle_route_change(route_event)

        # Debe instanciar la pantalla
        self.assertIsInstance(self.router.current_screen, DummyScreen1)
        self.assertTrue(self.router.current_screen.load_called)

        # El callback debe dispararse
        self.callback.assert_called_once_with(self.router.current_screen)

        # Simulamos cambio de ruta a /two
        prev_screen = self.router.current_screen
        route_event2 = Mock()
        route_event2.route = "/two"
        self.router._handle_route_change(route_event2)

        self.assertTrue(prev_screen.unload_called)
        self.assertIsInstance(self.router.current_screen, DummyScreen2)


if __name__ == "__main__":
    unittest.main()
