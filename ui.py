"""UI components and layout for the image editor."""

import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import os
from PIL import Image, ImageTk


class ImageEditorUI:
    """Handles all UI components and interactions."""

    def __init__(self, root, app):
        """Initialize UI components."""
        self.root = root
        self.app = app
        self.display_image = None
        self.slider = None
        self.canvas = None
        self.status = None

    def create_ui(self):
        """Create all UI components."""
        self._create_menu()
        self._create_controls()
        self._create_canvas()
        self._create_status_bar()

    def _create_menu(self):
        """Create menu bar."""
        menu = tk.Menu(self.root)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.app.open_image)
        file_menu.add_command(label="Save", command=self.app.save_image)
        file_menu.add_command(label="Save As", command=self.app.save_as_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.app.undo)
        edit_menu.add_command(label="Redo", command=self.app.redo)

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu)

    def _create_controls(self):
        """Create control panel with buttons."""
        panel = tk.Frame(self.root)
        panel.pack(side=tk.LEFT, padx=10, fill=tk.Y)

        # Effects section
        tk.Label(panel, text="Effects", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(panel, text="Grayscale", command=self.app.apply_grayscale).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Edge Detection", command=self.app.apply_edges).pack(fill=tk.X, pady=2)

        # Adjustments section
        tk.Label(panel, text="Adjustments", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(panel, text="Blur", command=self.app.show_blur_slider).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Brightness", command=self.app.show_brightness_slider).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Contrast", command=self.app.show_contrast_slider).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Resize / Scale", command=self.app.show_resize_slider).pack(fill=tk.X, pady=2)

        # Rotate section
        tk.Label(panel, text="Rotate", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(panel, text="Rotate 90°", command=lambda: self.app.rotate_image(90)).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Rotate 180°", command=lambda: self.app.rotate_image(180)).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Rotate 270°", command=lambda: self.app.rotate_image(270)).pack(fill=tk.X, pady=2)

        # Flip section
        tk.Label(panel, text="Flip", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Button(panel, text="Flip Horizontal", command=lambda: self.app.flip_image("horizontal")).pack(fill=tk.X, pady=2)
        tk.Button(panel, text="Flip Vertical", command=lambda: self.app.flip_image("vertical")).pack(fill=tk.X, pady=2)

        # Slider
        self.slider = tk.Scale(panel, orient=tk.HORIZONTAL, length=180)
        self.slider.pack(pady=10)
        self.slider.pack_forget()

    def _create_canvas(self):
        """Create canvas for image display."""
        self.canvas = tk.Canvas(self.root, bg="gray")
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def _create_status_bar(self):
        """Create status bar."""
        self.status = tk.Label(self.root, text="No image loaded",
                              bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def hide_slider(self):
        """Hide the slider."""
        self.slider.pack_forget()

    def show_blur_slider(self):
        """Configure and show blur slider."""
        self.slider.config(from_=1, to=25, label="Blur Intensity",
                          command=lambda v: self.app.apply_blur())
        self.slider.set(5)
        self.slider.pack()
        self.app.apply_blur()

    def show_brightness_slider(self):
        """Configure and show brightness slider."""
        self.slider.config(from_=-100, to=100, label="Brightness",
                          command=lambda v: self.app.adjust_brightness())
        self.slider.set(0)
        self.slider.pack()
        self.app.adjust_brightness()

    def show_contrast_slider(self):
        """Configure and show contrast slider."""
        self.slider.config(from_=-100, to=100, label="Contrast",
                          command=lambda v: self.app.adjust_contrast())
        self.slider.set(0)
        self.slider.pack()
        self.app.adjust_contrast()

    def show_resize_slider(self):
        """Configure and show resize slider."""
        self.slider.config(from_=10, to=200, label="Scale (%)",
                          command=lambda v: self.app.resize_image())
        self.slider.set(100)
        self.slider.pack()
        self.app.resize_image()

    def update_canvas(self, image):
        """Update canvas with new image."""
        self.canvas.delete("all")
        self.canvas.update_idletasks()

        cw, ch = self.canvas.winfo_width(), self.canvas.winfo_height()

        # Convert and display
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil = Image.fromarray(rgb)

        iw, ih = pil.size
        scale = min(cw / iw, ch / ih)
        pil = pil.resize((int(iw * scale), int(ih * scale)), Image.Resampling.LANCZOS)

        self.display_image = ImageTk.PhotoImage(pil)
        self.canvas.create_image(cw // 2, ch // 2, image=self.display_image, anchor=tk.CENTER)

    def update_status(self, text):
        """Update status bar text."""
        self.status.config(text=text)

    def ask_open_file(self):
        """Show open file dialog."""
        return filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp")]
        )

    def ask_save_file(self):
        """Show save file dialog."""
        return filedialog.asksaveasfilename(defaultextension=".png")

    def show_error(self, title, message):
        """Show error message."""
        messagebox.showerror(title, message)

    def show_info(self, title, message):
        """Show info message."""
        messagebox.showinfo(title, message)

    def get_slider_value(self):
        """Get current slider value."""
        return self.slider.get()
