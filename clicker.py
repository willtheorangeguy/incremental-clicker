
import tkinter as tk

class ClickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Clicker")

        self.count = tk.IntVar()
        self.count.set(0)

        self.label = tk.Label(master, textvariable=self.count, font=("Helvetica", 36))
        self.label.pack(pady=10)

        button_frame = tk.Frame(master)
        button_frame.pack()

        self.plus_button = tk.Button(button_frame, text="+", command=self.increment, font=("Helvetica", 16), width=3)
        self.plus_button.pack(side=tk.LEFT, padx=5)

        self.minus_button = tk.Button(button_frame, text="-", command=self.decrement, font=("Helvetica", 16), width=3)
        self.minus_button.pack(side=tk.RIGHT, padx=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Helvetica", 12))
        self.reset_button.pack(pady=5)

    def increment(self):
        self.count.set(self.count.get() + 1)

    def decrement(self):
        self.count.set(self.count.get() - 1)

    def reset(self):
        self.count.set(0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerApp(root)
    root.wm_attributes("-topmost", True)
    root.geometry("200x150")
    root.mainloop()
