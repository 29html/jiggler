import tkinter as tk
import pyautogui
import threading
import time

# Desactivar el fail-safe para evitar que el script se detenga si mueves el mouse a las esquinas
pyautogui.FAILSAFE = False

class MouseJiggler:
    def __init__(self, root):
        self.root = root
        self.root.title("Anti-Suspensión Pro")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        self.running = False
        self.intervalo = tk.IntVar(value=1)

        # Diseño de la interfaz
        tk.Label(root, text="Modo Super-Activo", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Label(root, text="Selecciona intervalo de acción:").pack()

        # Opciones de tiempo (minutos)
        frame_radio = tk.Frame(root)
        frame_radio.pack(pady=10)
        tk.Radiobutton(frame_radio, text="1 min", variable=self.intervalo, value=1).pack(side=tk.LEFT)
        tk.Radiobutton(frame_radio, text="3 min", variable=self.intervalo, value=3).pack(side=tk.LEFT)
        tk.Radiobutton(frame_radio, text="5 min", variable=self.intervalo, value=5).pack(side=tk.LEFT)

        # Botón de Inicio/Parada
        self.btn_accion = tk.Button(root, text="Iniciar", command=self.toggle, bg="green", fg="white", width=15)
        self.btn_accion.pack(pady=10)

        # Indicador de estado
        self.lbl_estado = tk.Label(root, text="Estado: Detenido", fg="red")
        self.lbl_estado.pack()

    def ejecutar_accion(self):
        """Función que realiza el movimiento y pulsa la tecla"""
        while self.running:
            # Espera el tiempo seleccionado (convertido a segundos)
            for _ in range(self.intervalo.get() * 60):
                if not self.running:
                    return
                time.sleep(1)
            
            # 1. Movimiento más amplio para asegurar detección (5 píxeles)
            pyautogui.moveRel(5, 5, duration=0.2)
            pyautogui.moveRel(-5, -5, duration=0.2)
            
            # 2. Pulsación de tecla 'Shift' (no escribe nada pero activa el sistema)
            pyautogui.press('shift')
            
            # Actualización visual en consola para depuración
            print(f"[{time.strftime('%H:%M:%S')}] Actividad enviada al sistema.")

    def toggle(self):
        """Alterna entre encendido y apagado"""
        if not self.running:
            self.running = True
            self.btn_accion.config(text="Detener", bg="red")
            self.lbl_estado.config(text=f"Activo cada {self.intervalo.get()} min", fg="green")
            
            # Iniciar hilo secundario
            self.thread = threading.Thread(target=self.ejecutar_accion, daemon=True)
            self.thread.start()
        else:
            self.running = False
            self.btn_accion.config(text="Iniciar", bg="green")
            self.lbl_estado.config(text="Estado: Detenido", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseJiggler(root)
    root.mainloop()
