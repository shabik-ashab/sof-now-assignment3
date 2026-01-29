"""Entry point for the Image Editor application."""

import tkinter as tk
from app import ImageEditorApp


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
