"""Image processing operations using OpenCV."""

import cv2


class ImageProcessor:
    """Handles all OpenCV image operations."""

    @staticmethod
    def to_grayscale(image):
        """Convert image to grayscale."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def apply_blur(image, intensity):
        """Apply Gaussian blur to image."""
        k = max(1, int(intensity))
        if k % 2 == 0:
            k += 1
        return cv2.GaussianBlur(image, (k, k), 0)

    @staticmethod
    def detect_edges(image):
        """Detect edges using Canny edge detection."""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 100, 200)

    @staticmethod
    def adjust_brightness(image, value):
        """Adjust image brightness."""
        return cv2.convertScaleAbs(image, alpha=1, beta=value)

    @staticmethod
    def adjust_contrast(image, value):
        """Adjust image contrast."""
        alpha = max(0.1, 1 + value / 100)
        return cv2.convertScaleAbs(image, alpha=alpha, beta=0)

    @staticmethod
    def rotate_image(image, angle):
        """Rotate image by specified angle (90, 180, 270)."""
        if angle == 90:
            return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            return cv2.rotate(image, cv2.ROTATE_180)
        elif angle == 270:
            return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        return image

    @staticmethod
    def flip_image(image, mode):
        """Flip image horizontally or vertically."""
        if mode == "horizontal":
            return cv2.flip(image, 1)
        elif mode == "vertical":
            return cv2.flip(image, 0)
        return image

    @staticmethod
    def resize_image(image, scale_percent):
        """Resize image by percentage scale."""
        scale = scale_percent / 100
        w = int(image.shape[1] * scale)
        h = int(image.shape[0] * scale)
        return cv2.resize(image, (w, h), interpolation=cv2.INTER_AREA)
