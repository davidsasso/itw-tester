class UnknownError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PrinterOpenError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PrinterZPLTemplateError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class PrinterDriverError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
class PrinterZPLFileError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message