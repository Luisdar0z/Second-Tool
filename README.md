# Conversor de Segundos

Aplicación de escritorio ligera que convierte:

- Segundos a formato `HH:MM:SS`.
- Tiempo `HH:MM:SS` a segundos totales.
- Genera múltiples valores aleatorios de segundos entre 1 y un máximo.

La interfaz usa Flask + PyWebView para ejecutar un servidor local y mostrar una ventana nativa sin consola.

---

## Prerrequisitos

- Python ≥ 3.7 instalado.
- `pip` (gestor de paquetes).
- Opcional: `icon.ico` en el directorio raíz para el empaquetado.

---

## Instalación de dependencias

```powershell
pip install -r requirements.txt
```

Esto instalará:
- Flask
- PyWebView

---

## Ejecución en desarrollo

```powershell
python app.py
```

Esto levantará la ventana nativa con la UI.

---

## Empaquetar en un `.exe` con PyInstaller

1. Instala PyInstaller (si no lo tienes):
   ```powershell
   pip install pyinstaller
   ```

2. Empaqueta tu proyecto:
   ```powershell
   pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --name conversor-gui app.py
   ```

3. (Opcional) Con icono personalizado:
   ```powershell
   pyinstaller --onefile --windowed --add-data "templates;templates" --add-data "static;static" --icon icon.ico --name conversor-gui app.py
   ```

4. El ejecutable resultante estará en `dist/conversor-gui.exe`.

---

## Uso del ejecutable

Simplemente haz doble clic en `conversor-gui.exe`. Se abrirá la ventana de la app sin mostrar la consola.

---

## Estructura del proyecto

```
segundos/  
├── app.py
├── requirements.txt
├── README.md
├── icon.ico         (opcional)
├── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/app.js
```

---

¡Disfruta de tu conversor de tiempos! Pull requests y mejoras son bienvenidas.
