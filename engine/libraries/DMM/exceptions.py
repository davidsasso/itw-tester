class UnknownError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class OpenError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ConfigureError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class CommandError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ResponseError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
class CloseError(Exception):
    """Custom exception class."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message