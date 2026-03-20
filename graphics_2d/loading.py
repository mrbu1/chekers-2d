import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk



try:
    import pygame
except ModuleNotFoundError:
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    frame = tk.Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Checkers 2d", font=("Arial", 36, "bold"), fg="white", bg="black").pack(pady=(0, 30))

    bar = ttk.Progressbar(frame, mode="indeterminate", length=500)
    bar.pack()

    tk.Label(frame, text="loading...", font=("Arial", 16), fg="white", bg="black").pack(pady=(20, 0))

    bar.start(12)

    install_error = None

    def install():
        global install_error
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "pygame"],
                check=True
            )
        except Exception as e:
            install_error = e
        finally:
            root.after(0, root.destroy)

    thread = threading.Thread(target=install)
    thread.start()

    root.mainloop()
    thread.join()

    if install_error:
        raise install_error

