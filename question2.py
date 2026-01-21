import cv2

# Task 1: Load Image
def load_image(path: str):
    # Load an image from the given file path and return it
    # Use cv2.imread() to read the image
    # Do not display the image here
    return None


# Task 2: Grayscale Conversion
def apply_grayscale(image):
    # Convert the input image to grayscale
    # Use cv2.cvtColor() with COLOR_BGR2GRAY
    return None


# Task 3: Gaussian Blur
def apply_gaussian_blur(image, kernel_size: int):
    # Apply Gaussian blur to the image
    # kernel_size controls the amount of blur (must be odd)
    # Use cv2.GaussianBlur()
    return None


# Task 4: Edge Detection
def apply_edge_detection(image, low_threshold: int, high_threshold: int):
    # Detect edges in the image using the Canny algorithm
    # Convert to grayscale first if needed
    # Use cv2.Canny() with the given thresholds
    return None


# Task 5: Brightness Adjustment
def adjust_brightness(image, value: int):
    # Change the brightness of the image
    # Positive value makes it brighter, negative makes it darker
    # Use cv2.convertScaleAbs()
    return None


# Task 6: Contrast Adjustment
def adjust_contrast(image, alpha: float):
    # Change the contrast of the image
    # alpha > 1 increases contrast, 0 < alpha < 1 decreases it
    # Use cv2.convertScaleAbs()
    return None


# Task 7: Rotate Image
def rotate_image(image, angle: int):
    # Rotate the image by 90, 180, or 270 degrees
    # Use cv2.rotate() or other OpenCV methods
    return None


# Task 8: Flip Image
def flip_image(image, direction: str):
    # Flip the image horizontally or vertically
    # direction = "horizontal" or "vertical"
    # Use cv2.flip()
    return None


# Task 9: Resize Image
def resize_image(image, scale: float):
    # Resize the image using the given scale factor
    # scale > 0 (0.5 = half size, 2.0 = double size)
    # Use cv2.resize()
    return None


# Main program
def main():
    # Path to the image file
    image_path = "image.jpg"

    # Load the image
    image = load_image(image_path)
    if image is None:
        print("Error: Image could not be loaded.")
        return

    # Apply image processing functions
    gray_image = apply_grayscale(image)
    blurred_image = apply_gaussian_blur(image, kernel_size=5)
    edge_image = apply_edge_detection(image, low_threshold=50, high_threshold=150)
    bright_image = adjust_brightness(image, value=30)
    contrast_image = adjust_contrast(image, alpha=1.5)
    rotated_image = rotate_image(image, angle=90)
    flipped_image = flip_image(image, direction="horizontal")
    resized_image = resize_image(image, scale=0.5)

    # Display all images
    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", gray_image)
    cv2.imshow("Blurred", blurred_image)
    cv2.imshow("Edges", edge_image)
    cv2.imshow("Brightness", bright_image)
    cv2.imshow("Contrast", contrast_image)
    cv2.imshow("Rotated", rotated_image)
    cv2.imshow("Flipped", flipped_image)
    cv2.imshow("Resized", resized_image)

    # Wait for key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
