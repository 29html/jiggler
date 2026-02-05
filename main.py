import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

class MouseJiggler:
    def __init__(self, root):
        self.root = root
        self.root.title("Anti-Suspensión")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        self.running = False
        self.intervalo = tk.IntVar(value=1)

        # Interfaz
        tk.Label(root, text="Evitar Suspensión", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Mover mouse cada (minutos):").pack()

        # Opciones de tiempo
        frame_radio = tk.Frame(root)
        frame_radio.pack(pady=10)
        tk.Radiobutton(frame_radio, text="1 min", variable=self.intervalo, value=1).pack(side=tk.LEFT)
        tk.Radiobutton(frame_radio, text="3 min", variable=self.intervalo, value=3).pack(side=tk.LEFT)
        tk.Radiobutton(frame_radio, text="5 min", variable=self.intervalo, value=5).pack(side=tk.LEFT)

        # Botones
        self.btn_accion = tk.Button(root, text="Iniciar", command=self.toggle, bg="green", fg="white", width=15)
        self.btn_accion.pack(pady=10)

        self.lbl_estado = tk.Label(root, text="Estado: Detenido", fg="red")
        self.lbl_estado.pack()

    def mover_mouse(self):
        while self.running:
            # Espera el tiempo seleccionado (minutos a segundos)
            for _ in range(self.intervalo.get() * 60):
                if not self.running: return
                time.sleep(1)
            
            # Movimiento sutil
            pyautogui.moveRel(1, 0, duration=0.2)
            pyautogui.moveRel(-1, 0, duration=0.2)

    def toggle(self):
        if not self.running:
            self.running = True
            self.btn_accion.config(text="Detener", bg="red")
            self.lbl_estado.config(text=f"Estado: Activo ({self.intervalo.get()} min)", fg="green")
            # Usamos un hilo para que la ventana no se congele
            self.thread = threading.Thread(target=self.mover_mouse, daemon=True)
            self.thread.start()
        else:
            self.running = False
            self.btn_accion.config(text="Iniciar", bg="green")
            self.lbl_estado.config(text="Estado: Detenido", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseJiggler(root)
    root.mainloop()
