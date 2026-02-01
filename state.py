"""Image state management with undo/redo functionality."""


class ImageStateManager:
    """Manages current image and undo/redo stacks."""

    def __init__(self):
        """Initialize state manager."""
        self._current_image = None
        self._undo_stack = []
        self._redo_stack = []

    def set_image(self, image):
        """Set current image and save to undo stack."""
        if self._current_image is not None:
            self._undo_stack.append(self._current_image.copy())
        self._current_image = image.copy()
        self._redo_stack.clear()

    def get_image(self):
        """Get current image."""
        return self._current_image

    def undo(self):
        """Undo last operation."""
        if self._undo_stack:
            self._redo_stack.append(self._current_image.copy())
            self._current_image = self._undo_stack.pop()
        return self._current_image

    def redo(self):
        """Redo last undone operation."""
        if self._redo_stack:
            self._undo_stack.append(self._current_image.copy())
            self._current_image = self._redo_stack.pop()
        return self._current_image
