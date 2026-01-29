"""Image processing operations using OpenCV. """

import cv2


class ImageProcessor:
    """Handles all OpenCV image operations."""

    @staticmethod
    def to_grayscale(image):
        """Convert image to grayscale."""

    @staticmethod
    def apply_blur(image, intensity):
        """Apply Gaussian blur to image."""

    @staticmethod
    def detect_edges(image):
        """Detect edges using Canny edge detection."""

    @staticmethod
    def adjust_brightness(image, value):
        """Adjust image brightness."""

    @staticmethod
    def adjust_contrast(image, value):
        """Adjust image contrast."""

    @staticmethod
    def rotate_image(image, angle):
        """Rotate image by specified angle (90, 180, 270)."""

    @staticmethod
    def flip_image(image, mode):
        """Flip image horizontally or vertically."""

    @staticmethod
    def resize_image(image, scale_percent):
        """Resize image by percentage scale."""
