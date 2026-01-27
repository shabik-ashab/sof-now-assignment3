import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import os


# =========================
# Image Processing Logic
# =========================
class ImageProcessor:
    """Handles all OpenCV image operations"""

    def to_grayscale(self, image):
        pass

    def apply_blur(self, image, intensity):
        pass

    def detect_edges(self, image):
        pass

    def adjust_brightness(self, image, value):
        pass

    def adjust_contrast(self, image, value):
        pass

    def rotate_image(self, image, angle):
        pass

    def flip_image(self, image, mode):
        pass

    def resize_image(self, image, scale):
        pass


# =========================
# Image State Management
# =========================
class ImageStateManager:
    """Manages current image and undo/redo stacks"""

    def __init__(self):
        self._current_image = None
        self._undo_stack = []
        self._redo_stack = []

    def set_image(self, image):
        if self._current_image is not None:
            self._undo_stack.append(self._current_image)
        self._current_image = image
        self._redo_stack.clear()

    def get_image(self):
        return self._current_image

    def undo(self):
        if self._undo_stack:
            self._redo_stack.append(self._current_image)
            self._current_image = self._undo_stack.pop()
        return self._current_image

    def redo(self):
        if self._redo_stack:
            self._undo_stack.append(self._current_image)
            self._current_image = self._redo_stack.pop()
        return self._current_image


# =========================
# Main Application (GUI)
# =========================
class ImageEditorApp:
    """Main application class"""

    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")
        self.root.geometry("900x600")

        self.processor = ImageProcessor()
        self.state_manager = ImageStateManager()

        self.display_image = None

        self._create_ui()

    # ---------- UI SETUP ----------
    def _create_ui(self):
        self._create_menu()
        self._create_canvas()
        self._create_controls()
        self._create_status_bar()

    def _create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Save As", command=self.save_as_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu_bar)

    def _create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="gray")
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def _create_controls(self):
        panel = tk.Frame(self.root)
        panel.pack(side=tk.LEFT, padx=10)

        tk.Button(panel, text="Grayscale", command=self.apply_grayscale).pack(pady=2)
        tk.Button(panel, text="Blur", command=self.apply_blur).pack(pady=2)
        tk.Button(panel, text="Edge Detection", command=self.apply_edges).pack(pady=2)
        tk.Button(panel, text="Rotate", command=self.rotate_image).pack(pady=2)
        tk.Button(panel, text="Flip", command=self.flip_image).pack(pady=2)

        self.slider = tk.Scale(panel, from_=1, to=20,
                               orient=tk.HORIZONTAL, label="Intensity")
        self.slider.pack(pady=5)


    def _create_status_bar(self):
        self.status_bar = tk.Label(
            self.root,
            text="No image loaded",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ---------- FILE OPERATIONS ----------
    def open_image(self):
        # Ask user to select an image file
        file_path = filedialog.askopenfilename(
            title="Open Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )

        if not file_path:
            return

        # Load image using OpenCV
        image = cv2.imread(file_path)
        if image is None:
            messagebox.showerror("Error", "Failed to load image")
            return

        # Store image in state manager
        self.state_manager.set_image(image)

        # Prepare canvas size
        self.canvas.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Convert image to RGB for Tkinter
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)

        # Resize image to fit canvas while keeping aspect ratio
        img_w, img_h = image_pil.size
        scale = min(canvas_width / img_w, canvas_height / img_h)
        new_size = (int(img_w * scale), int(img_h * scale))

        image_resized = image_pil.resize(
            new_size,
            Image.Resampling.LANCZOS
        )

        # Convert to Tkinter image and display
        self.display_image = ImageTk.PhotoImage(image_resized)
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=self.display_image,
            anchor=tk.CENTER
        )

        # Update status bar
        h, w = image.shape[:2]
        filename = os.path.basename(file_path)
        self.status_bar.config(
            text=f"File: {filename} | Size: {w}x{h}"
        )

    def save_image(self):
        pass

    def save_as_image(self):
        pass

    # ---------- IMAGE ACTIONS ----------
    def apply_grayscale(self):
        pass

    def apply_blur(self):
        pass

    def apply_edges(self):
        pass

    def rotate_image(self):
        pass

    def flip_image(self):
        pass

    # ---------- UNDO / REDO ----------
    def undo(self):
        pass

    def redo(self):
        pass

    # ---------- DISPLAY ----------
    def update_canvas(self, image):
        pass


# =========================
# Application Entry Point
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
