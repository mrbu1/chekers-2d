import tkinter as tk

def choose_mode():
    root = tk.Tk()
    root.geometry("900x600")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    frame = tk.Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(
        frame,
        text="Choose mode",
        font=("Arial", 36, "bold"),
        fg="white",
        bg="black"
    )
    title.pack(pady=(0, 40))

    result = {"is2dmode": False}

    def open_2d():
        result["is2dmode"] = True
        root.destroy()

    def open_term():
        result["is2dmode"] = False
        root.destroy()

    btn_2d = tk.Button(
        frame,
        text="2D (NEW!)",
        font=("Arial", 18, "bold"),
        width=18,
        height=2,
        bg="white",
        fg="black",
        bd=0,
        activebackground="#349a30",
        activeforeground="black",
        cursor="hand2",
        command=open_2d
    )
    btn_2d.pack(pady=(0, 20))

    btn_terminal = tk.Button(
        frame,
        text="Terminal",
        font=("Arial", 18, "bold"),
        width=18,
        height=2,
        bg="white",
        fg="black",
        bd=0,
        activebackground="#349a30",
        activeforeground="black",
        cursor="hand2",
        command=open_term
    )
    btn_terminal.pack()

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()
    return result["is2dmode"]