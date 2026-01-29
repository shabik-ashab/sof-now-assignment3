"""Main application class for the image editor."""

import cv2
import os
from processors import ImageProcessor
from state import ImageStateManager
from ui import ImageEditorUI


class ImageEditorApp:
    """Main application controller."""

    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Image Editor")
        self.root.geometry("1000x650")

        # Core components
        self.processor = ImageProcessor()
        self.state = ImageStateManager()
        self.current_file = None

        # UI
        self.ui = ImageEditorUI(root, self)
        self.ui.create_ui()

    # ===== File Operations =====
    def open_image(self):
        """Open an image file."""
        path = self.ui.ask_open_file()
        if not path:
            return

        image = cv2.imread(path)
        if image is None:
            self.ui.show_error("Error", "Cannot load image")
            return

        self.current_file = path
        self.state.set_image(image)
        self.ui.update_canvas(image)

        h, w = image.shape[:2]
        self.ui.update_status(f"{os.path.basename(path)} | {w}x{h}")

    def save_image(self):
        """Save the current image."""
        if self.current_file:
            cv2.imwrite(self.current_file, self.state.get_image())
            self.ui.show_info("Saved", "Image saved successfully")
        else:
            self.save_as_image()

    def save_as_image(self):
        """Save the current image with a new name."""
        image = self.state.get_image()
        if image is None:
            return
        path = self.ui.ask_save_file()
        if path:
            cv2.imwrite(path, image)
            self.current_file = path
            self.ui.show_info("Saved", "Image saved successfully")

    # ===== Image Processing =====
    def apply_grayscale(self):
        """Apply grayscale effect."""
        img = self.processor.to_grayscale(self.state.get_image())
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        self.state.set_image(img)
        self.ui.update_canvas(img)

    def apply_blur(self):
        """Apply blur effect based on slider value."""
        img = self.processor.apply_blur(self.state.get_image(), self.ui.get_slider_value())
        self.ui.update_canvas(img)

    def apply_edges(self):
        """Apply edge detection."""
        edges = self.processor.detect_edges(self.state.get_image())
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        self.state.set_image(img)
        self.ui.update_canvas(img)

    def adjust_brightness(self):
        """Adjust brightness based on slider value."""
        img = self.processor.adjust_brightness(self.state.get_image(), self.ui.get_slider_value())
        self.ui.update_canvas(img)

    def adjust_contrast(self):
        """Adjust contrast based on slider value."""
        img = self.processor.adjust_contrast(self.state.get_image(), self.ui.get_slider_value())
        self.ui.update_canvas(img)

    def rotate_image(self, angle):
        """Rotate image by angle."""
        img = self.processor.rotate_image(self.state.get_image(), angle)
        self.state.set_image(img)
        self.ui.update_canvas(img)

    def flip_image(self, mode):
        """Flip image (horizontal or vertical)."""
        img = self.processor.flip_image(self.state.get_image(), mode)
        self.state.set_image(img)
        self.ui.update_canvas(img)

    def resize_image(self):
        """Resize image based on slider value."""
        img = self.processor.resize_image(self.state.get_image(), self.ui.get_slider_value())
        self.ui.update_canvas(img)

    # ===== Undo/Redo =====
    def undo(self):
        """Undo last operation."""
        img = self.state.undo()
        if img is not None:
            self.ui.update_canvas(img)

    def redo(self):
        """Redo last undone operation."""
        img = self.state.redo()
        if img is not None:
            self.ui.update_canvas(img)

    # ===== Slider Actions =====
    def show_blur_slider(self):
        """Show blur slider."""
        self.ui.show_blur_slider()

    def show_brightness_slider(self):
        """Show brightness slider."""
        self.ui.show_brightness_slider()

    def show_contrast_slider(self):
        """Show contrast slider."""
        self.ui.show_contrast_slider()

    def show_resize_slider(self):
        """Show resize slider."""
        self.ui.show_resize_slider()
