# Flet Layout System

Sistema de layouts responsive profesional para aplicaciones **Flet**. Permite componer layouts con barras superior, inferior, izquierda y derecha de forma declarativa y con soporte completo de responsividad.

---

## Características

- ✅ Soporte para 4 barras simultáneas (top, bottom, left, right)
- ✅ Responsive automático con 3 breakpoints (móvil, tablet, desktop)
- ✅ Sidebars colapsables con animaciones suaves
- ✅ Patrón Builder fluido y legible
- ✅ Helpers listos para usar (navbar, sidebar, footer)
- ✅ Cambio de contenido dinámico sin reconstruir el layout
- ✅ Sin dependencias adicionales

---

## Instalación

```bash
pip install flet
```

---

## Uso Básico

```python
import flet as ft
from layout_system import LayoutBuilder
from layout_helpers import create_simple_navbar, setup_responsive_layout

def main(page: ft.Page):
    page.padding = 0

    content = ft.Container(
        content=ft.Text("Mi App"),
        padding=20,
        expand=True,
    )

    layout = (
        LayoutBuilder()
        .with_content(content)
        .with_top_bar(create_simple_navbar("Mi App"))
        .build()
    )

    page.add(layout)
    setup_responsive_layout(layout, page)

ft.app(target=main)
```

---

## Uso Completo (todas las barras)

```python
layout = (
    LayoutBuilder()
    .with_content(mi_contenido)
    .with_top_bar(navbar, height=60, bgcolor=ft.Colors.INDIGO_700)
    .with_left_bar(sidebar, width=250, bgcolor=ft.Colors.GREY_50)
    .with_right_bar(panel_derecho, width=300)
    .with_bottom_bar(footer, height=50)
    .with_responsive_config(
        breakpoint_mobile=600,
        breakpoint_tablet=1024,
        collapse_sidebars_on_mobile=True,
        collapse_sidebars_on_tablet=True,
    )
    .build()
)
```

---

## API Completa

### `ResponsiveLayout`

| Parámetro | Tipo | Default | Descripción |
|---|---|---|---|
| `content` | `ft.Control` | — | Contenido principal (**obligatorio**) |
| `top_bar` | `ft.Control` | `None` | Barra superior |
| `bottom_bar` | `ft.Control` | `None` | Barra inferior |
| `left_bar` | `ft.Control` | `None` | Barra lateral izquierda |
| `right_bar` | `ft.Control` | `None` | Barra lateral derecha |
| `top_bar_height` | `int` | `60` | Altura de la barra superior (px) |
| `bottom_bar_height` | `int` | `60` | Altura de la barra inferior (px) |
| `left_bar_width` | `int` | `250` | Ancho de la barra izquierda (px) |
| `right_bar_width` | `int` | `250` | Ancho de la barra derecha (px) |
| `*_bgcolor` | `str` | `None` | Color de fondo de cada barra |
| `breakpoint_mobile` | `int` | `600` | Ancho máximo para modo móvil (px) |
| `breakpoint_tablet` | `int` | `1024` | Ancho máximo para modo tablet (px) |
| `collapse_sidebars_on_mobile` | `bool` | `True` | Colapsa sidebars en móvil |
| `collapse_sidebars_on_tablet` | `bool` | `False` | Colapsa sidebars en tablet |
| `left_bar_collapsible` | `bool` | `True` | Permite colapso manual del sidebar izq. |
| `right_bar_collapsible` | `bool` | `True` | Permite colapso manual del sidebar der. |
| `animate_transitions` | `bool` | `True` | Anima las transiciones de colapso |

**Métodos públicos:**

```python
layout.toggle_left_sidebar()   # Alterna visibilidad del sidebar izquierdo
layout.toggle_right_sidebar()  # Alterna visibilidad del sidebar derecho
layout.on_resize(width: int)   # Llamar al cambiar page.width
```

**Propiedades:**

```python
layout.is_mobile   # bool
layout.is_tablet   # bool
layout.is_desktop  # bool
```

---

### `LayoutBuilder`

Métodos encadenables:

```python
.with_content(content)
.with_top_bar(bar, height=60, bgcolor=None)
.with_bottom_bar(bar, height=60, bgcolor=None)
.with_left_bar(bar, width=250, bgcolor=None, collapsible=True)
.with_right_bar(bar, width=250, bgcolor=None, collapsible=True)
.with_responsive_config(breakpoint_mobile, breakpoint_tablet,
                         collapse_sidebars_on_mobile, collapse_sidebars_on_tablet)
.build()  # → ResponsiveLayout
```

---

### Helpers (`layout_helpers.py`)

```python
# Conecta el resize de la página al layout automáticamente
setup_responsive_layout(layout, page)

# Crea una barra superior con botón de menú opcional
create_simple_navbar(title, on_menu_click=None, show_menu=True)

# Crea un sidebar con lista de ítems {icon, label}
create_simple_sidebar(items, on_click=None)

# Crea un footer centrado
create_footer(text="© 2026")

# Valida rangos de dimensiones (lanza ValueError si son inválidos)
validate_layout_params(left_bar_width, right_bar_width, top_bar_height, bottom_bar_height)
```

---

## Comportamiento Responsive

| Ancho de ventana | Estado | Sidebars |
|---|---|---|
| `< 600 px` | `is_mobile = True` | Colapsados (si `collapse_sidebars_on_mobile=True`) |
| `600–1023 px` | `is_tablet = True` | Colapsados (si `collapse_sidebars_on_tablet=True`) |
| `≥ 1024 px` | `is_desktop = True` | Visibles |

---

## Contenido Dinámico

Para cambiar contenido sin reconstruir el layout, usa un contenedor en el que actualizas `content`:

```python
content_area = ft.Container(expand=True)

layout = LayoutBuilder().with_content(content_area).build()

# Cambiar vista:
content_area.content = nueva_vista()
page.update()
```

---

## Barras Personalizadas

Cualquier `ft.Control` puede usarse como barra. Ejemplo con `AppBar` de Flet:

```python
appbar = ft.AppBar(
    title=ft.Text("Mi App"),
    center_title=False,
    bgcolor=ft.Colors.SURFACE_VARIANT,
)

layout = LayoutBuilder().with_content(content).with_top_bar(appbar, height=56).build()
```

---

## Tips y Mejores Prácticas

1. **Usa siempre `setup_responsive_layout()`** en lugar de configurar `page.on_resize` manualmente.
2. **Evita closures circulares** con el patrón de diccionario de estado:
   ```python
   state = {"layout": None}
   def toggle(): state["layout"].toggle_left_sidebar()
   state["layout"] = LayoutBuilder()...build()
   ```
3. **No añadas `padding` en la estructura del layout** — añádelo al contenido.
4. **No pases colores hardcodeados** — usa los parámetros `bgcolor` para que sea configurable.

---

## Ejemplos incluidos

| Archivo | Descripción |
|---|---|
| `ejemplo_simple.py` | App mínima con solo barra superior |
| `ejemplo_dashboard.py` | Dashboard completo con sidebar, navbar, footer y 4 vistas |
