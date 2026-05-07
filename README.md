# Proyecto de Automatización QA - SauceDemo 🚀

## 📝 Propósito del Proyecto
Este proyecto es parte de la pre-entrega final del curso de Automatización. El objetivo es validar el flujo principal que realiza un usuario en [SauceDemo](https://www.saucedemo.com/): desde el inicio de sesión seguro y la validación del catálogo de productos, hasta la interacción y verificación del carrito de compras.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Framework de Pruebas:** Pytest
* **Herramienta de Automatización:** Selenium WebDriver
* **Reportes:** Pytest-HTML

## 📁 Estructura del Proyecto
* `tests/`: Scripts de prueba (Login, Inventario y Carrito).
* `utils/`: Lógica de interacción con elementos (LoginPage).
* `evidencias/`: Capturas de pantalla generadas automáticamente durante la ejecución de los tests.
* `conftest.py`: Configuración del WebDriver y Fixtures para la reutilización de código.
* `pytest.ini`: Configuración de parámetros de ejecución y generación de reportes.

## ⚙️ Instalación de Dependencias
Para ejecutar este proyecto correctamente, es necesario contar con Python instalado y ejecutar el siguiente comando en la terminal:

```bash
pip install selenium pytest pytest-html