"""
ui.py
ImageEditorUI class for Tkinter-based Image Editor
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2


class ImageEditorUI:
    """
    Handles all UI components for the Image Editor application.
    """

    def __init__(self, root, app):
        """
        Initialize the UI with root window and application controller.
        """
        self.root = root
        self.app = app
        self.root.title("Image Editor")
        self.root.geometry("1000x700")

        self.slider_value = tk.IntVar(value=50)
        self.image_on_canvas = None

        self.create_ui()

    def create_ui(self):
        """Build the complete UI layout."""
        self._create_menu()
        self._create_controls()
        self._create_canvas()
        self._create_status_bar()

    def _create_menu(self):
        """Create File and Edit menus."""
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.app.open_image)
        file_menu.add_command(label="Save", command=self.app.save_image)
        file_menu.add_command(label="Save As", command=self.app.save_image_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.app.undo)
        edit_menu.add_command(label="Redo", command=self.app.redo)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def _create_controls(self):
        """Create control panel with buttons and sliders."""
        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(
            control_frame,
            text="Image Controls",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        ttk.Button(control_frame, text="Grayscale", command=self.app.apply_grayscale).pack(fill=tk.X, pady=2)
        ttk.Button(control_frame, text="Blur", command=self.app.apply_blur).pack(fill=tk.X, pady=2)
        ttk.Button(control_frame, text="Edge Detection", command=self.app.apply_edge).pack(fill=tk.X, pady=2)

        ttk.Button(
            control_frame,
            text="Flip Horizontal",
            command=lambda: self.app.apply_flip("h")
        ).pack(fill=tk.X, pady=2)

        ttk.Button(
            control_frame,
            text="Flip Vertical",
            command=lambda: self.app.apply_flip("v")
        ).pack(fill=tk.X, pady=2)

        ttk.Button(
            control_frame,
            text="Rotate 90°",
            command=lambda: self.app.apply_rotate(90)
        ).pack(fill=tk.X, pady=2)

        ttk.Label(control_frame, text="Brightness / Contrast").pack(pady=5)

        ttk.Scale(
            control_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.slider_value
        ).pack(fill=tk.X)

        ttk.Button(
            control_frame,
            text="Apply Adjustment",
            command=self.app.apply_adjustment
        ).pack(fill=tk.X, pady=5)

    def _create_canvas(self):
        """Create canvas for image display."""
        self.canvas = tk.Canvas(self.root, bg="gray")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def _create_status_bar(self):
        """Create status bar."""
        self.status_var = tk.StringVar(value="Ready")

        status_bar = ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def update_canvas(self, image):
        """
        Display image on canvas.

        :param image: OpenCV image (NumPy array)
        """
        self.canvas.delete("all")

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image_rgb)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        pil_image.thumbnail((canvas_width, canvas_height))

        self.image_on_canvas = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=self.image_on_canvas,
            anchor=tk.CENTER
        )

    def update_status(self, message):
        """Update status bar message."""
        self.status_var.set(message)

    def get_slider_value(self):
        """Return current slider value."""
        return self.slider_value.get()

    def ask_open_file(self):
        """Show open file dialog."""
        return filedialog.askopenfilename(
            filetypes=[
                ("Image Files", "*.jpg *.png *.bmp"),
                ("All Files", "*.*")
            ]
        )

    def ask_save_file(self):
        """Show save file dialog."""
        return filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[
                ("JPEG", "*.jpg"),
                ("PNG", "*.png"),
                ("Bitmap", "*.bmp")
            ]
        )

    def show_error(self, message):
        """Show error message dialog."""
        messagebox.showerror("Error", message)

    def show_info(self, message):
        """Show information message dialog."""
        messagebox.showinfo("Information", message)
