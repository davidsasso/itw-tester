

class PreUUTLoopException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class PreUUTException(Exception):
    pass

class MainException(Exception):
    pass

class PostUUTException(Exception):
    pass

class PostUUTLoopException(Exception):
    pass
