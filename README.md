# Flet Base Template

Plantilla base para crear aplicaciones desktop/web con Flet, con un sistema
de layouts responsive (top/left/right/bottom bars), helpers reutilizables,
temas y soporte simple de traducciones (CSV).

**Contenido del repositorio**
- `layout/`: implementación del sistema de layout (`layout_system.py`), helpers
	para navbar/sidebar/footer (`layout_helpers.py`) y ejemplos de uso:
	- [layout/ejemplo_simple.py](layout/ejemplo_simple.py) — ejemplo minimalista.
	- [layout/ejemplo_dashboard.py](layout/ejemplo_dashboard.py) — dashboard completo.
- `components/`: componentes reutilizables (UI).
- `themes/`: definiciones y helpers de temas.
- `translations/`: sistema simple para traducciones mediante CSV.
- `test/`: pruebas unitarias de ejemplo.

**Objetivo**
Proveer una base clara y modular para construir interfaces tipo dashboard o apps
con varias barras (top, left, bottom, right) y comportamiento responsive sin
duplicar la gestión de scroll o estado entre vistas.

**Requisitos**
- Python 3.10+ (o la versión compatible que uses con Flet)
- `flet` (recomendado instalar en un virtualenv)

Instalar dependencias mínimas:

```
python -m pip install --upgrade pip
pip install flet
```

Si prefieres usar el virtualenv incluido en `env/`, actívalo antes de instalar.

**Ejecutar los ejemplos**

- Ejemplo simple (barra superior + contenido):

```
python layout/ejemplo_simple.py
```

- Ejemplo dashboard (top bar, sidebar colapsable, footer y vistas dinámicas):

```
python layout/ejemplo_dashboard.py
```

Ambos ejemplos usan `LayoutBuilder` (ver más abajo) y los helpers en
`layout_helpers.py` para construir las barras y gestionar el resize.

**Breve guía de uso**

1. Crear el contenido principal (una `ft.Control` — p.ej. `ft.Container` o
	 `ft.Column`) sin gestionar scroll interno: el layout gestorará el scroll.
2. Construir el layout con `LayoutBuilder` usando los métodos encadenados.
3. Conectar el resize de la página con `setup_responsive_layout()`.

Ejemplo mínimo de uso:

```
import flet as ft
from layout_system import LayoutBuilder
from layout_helpers import create_simple_navbar, setup_responsive_layout

def main(page: ft.Page):
		content = ft.Container(content=ft.Text('Hola Mundo'), padding=20)
		navbar = create_simple_navbar('Mi App')

		layout = (
				LayoutBuilder()
				.with_content(content)
				.with_top_bar(navbar, height=60, bgcolor=ft.Colors.BLUE_700)
				.build()
		)

		page.add(layout)
		setup_responsive_layout(layout, page)

if __name__ == '__main__':
		ft.app(target=main)
```

**API rápida (principales piezas)**

- `layout/layout_system.py`
	- `ResponsiveLayout`: clase principal que gestiona top/left/right/bottom bars,
		animaciones, colapso automático por breakpoints y el contenido central.
	- `LayoutBuilder`: builder fluido con métodos `with_content()`,
		`with_top_bar()`, `with_left_bar()`, `with_bottom_bar()`, `with_responsive_config()`,
		`with_transitions()` y `build()`.

- `layout/layout_helpers.py`
	- `setup_responsive_layout(layout, page)`: conecta el resize de la página
		con `layout.on_resize()` y hace la inicialización.
	- `create_simple_navbar(title, on_menu_click=None, show_menu=True)`: crea
		una barra superior básica.
	- `create_simple_sidebar(items, on_click=None)`: crea un sidebar con ítems
		(cada item: `{'icon': ft.Icons.*, 'label': 'Texto'}`) y callback `on_click(idx)`.
	- `create_footer(text)`: footer simple.

**Consejos y buenas prácticas**
- No configures scroll dentro de las vistas: el `ResponsiveLayout` gestiona el
	scroll vertical/horizontal del contenido central.
- Usa `AnimatedSwitcher` (como en `ejemplo_dashboard.py`) para cambiar vistas
	sin reconstruir el layout completo.
- Validar valores de dimensiones con `validate_layout_params()` si los expones
	a usuarios o configuración dinámica.

**Temas y traducciones**
- Revisa `themes/themes.py` para crear/editar paletas y modos.
- El directorio `translations/` contiene utilidades para cargar CSVs de
	traducción. Puedes adaptar el formato CSV según tus necesidades.

**Tests**
- Hay ejemplos de tests en `test/test_translation.py`. Ejecuta con `pytest`
	tras instalar `pytest` si quieres validar el sistema de traducciones.

**Siguientes pasos sugeridos**
- Añadir un `requirements.txt` o `pyproject.toml` si vas a publicar/compartir
	esta plantilla.  
- Integrar más ejemplos con gráficos y fuentes de datos reales.

Si quieres, puedo:
- Añadir un `requirements.txt` con las dependencias detectadas.
- Ejecutar las pruebas o ajustar el README con instrucciones adicionales.

---
_Generado: plantilla README con ejemplos y guía rápida para empezar._
