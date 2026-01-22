import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

# Keep a reference to the current image
current_image = None  # This will store the OpenCV image
display_image = None  # This will store the Tkinter-compatible image

# Main Window & Menu
def create_main_window():
    root = tk.Tk()
    root.title("Image Editor")
    root.geometry("800x600")
    return root

def open_file(canvas, status_bar):
    global current_image, display_image

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Open Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_path:
        return

    # Read image with OpenCV
    current_image = cv2.imread(file_path)
    if current_image is None:
        show_message("Error", "Failed to load image", type="error")
        return

    # Make sure canvas size is available
    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)

    # Resize image to fit canvas while keeping aspect ratio
    img_w, img_h = image_pil.size
    scale_w = canvas_width / img_w
    scale_h = canvas_height / img_h
    scale = min(scale_w, scale_h)

    new_width = int(img_w * scale)
    new_height = int(img_h * scale)

    image_resized = image_pil.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    # Convert to Tkinter-compatible image
    display_image = ImageTk.PhotoImage(image_resized)

    # Clear canvas and display image in center
    canvas.delete("all")
    canvas.create_image(
        canvas_width // 2,
        canvas_height // 2,
        anchor=tk.CENTER,
        image=display_image
    )

    # Update status bar
    height, width = current_image.shape[:2]
    update_status_bar(
        status_bar,
        filename=file_path,
        width=width,
        height=height,
        format=file_path.split('.')[-1].upper()
    )


def create_menu_bar(root, canvas, status_bar):
    menu_bar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=lambda: open_file(canvas, status_bar))
    file_menu.add_command(label="Save", command=lambda: None)  # To implement later
    file_menu.add_command(label="Save As", command=lambda: None)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Edit Menu
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Undo", command=lambda: None)
    edit_menu.add_command(label="Redo", command=lambda: None)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    root.config(menu=menu_bar)


# Image Display Area
def create_image_display(root):
    canvas = tk.Canvas(root, width=600, height=400, bg="gray")
    canvas.pack(pady=10)
    return canvas


# Control Panel & Slider
def create_control_panel(root):
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=10)

    tk.Button(frame, text="Grayscale", command=lambda: None).pack(pady=2)
    tk.Button(frame, text="Blur", command=lambda: None).pack(pady=2)
    tk.Button(frame, text="Rotate", command=lambda: None).pack(pady=2)
    tk.Button(frame, text="Flip", command=lambda: None).pack(pady=2)

    return frame

def create_slider(root):
    frame = tk.Frame(root)
    frame.pack(side=tk.RIGHT, padx=10)

    slider = tk.Scale(frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Effect Intensity")
    slider.pack(pady=5)

    return slider


# Status Bar & Messages
def create_status_bar(root):
    status = tk.Label(root, text="No image loaded", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)
    return status

def update_status_bar(status_bar, filename="", width=0, height=0, format=""):
    status_bar.config(text=f"File: {filename} | Size: {width}x{height} | Format: {format}")

def show_message(title, message, type="info"):
    if type == "info":
        messagebox.showinfo(title, message)
    elif type == "error":
        messagebox.showerror(title, message)


# Main program
def main():
    root = create_main_window()

    status_bar = create_status_bar(root)
    canvas = create_image_display(root)
    control_panel = create_control_panel(root)
    slider = create_slider(root)
    create_menu_bar(root, canvas, status_bar)

    root.mainloop()


if __name__ == "__main__":
    main()
