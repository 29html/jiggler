## 1. Instala las dependencias
pip install pyautogui pygetwindow pytweening mouseinfo pyinstaller

## 2. Uso de interfaz gráfica (sin consola)

Como ahora tenemos una interfaz gráfica, no queremos que se abra una ventana de consola negra detrás de nuestra aplicación.
Para evitarlo, usaremos el parámetro --noconsole.

Ejecuta este comando en tu terminal:
```bash
commando: pyinstaller --onefile --noconsole main.py

## Parámetros utilizados:
## --onefile: Empaqueta todo en un solo archivo .exe.
## --noconsole: Oculta la ventana de comandos, dejando solo la ventana del programa.
```
## 3. Solución de problemas por dependencias:
Debería funcionar correctamente, pero en caso de que falle por un error de dependencias, ejecuta el siguiente comando:
```bash
python -m pip install pyautogui
```

## 4. Limpieza y recompilación
Borrar rastros anteriores
```bash
## Borrar rastros anteriores
rm -rf build dist
```

```bash
## Compilar de nuevo asegurando que Python vea el módulo
python -m PyInstaller --onefile --noconsole main.py
```

