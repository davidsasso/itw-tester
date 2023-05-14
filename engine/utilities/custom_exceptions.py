

class PreUUTLoopException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class PreUUTException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class MainException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class PostUUTException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class PostUUTLoopException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def exceptions_handler(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except PreUUTLoopException as e:
            print(f"[Error] An exception occurred in PreUUTLoop: {str(e)}")
            # handle the exception here, or re-raise it if necessary
        except PreUUTException as e:
            print(f"[Error] An exception occurred in PreUUT: {str(e)}")
            # handle the exception here, or re-raise it if necessary
        except MainException as e:
            print('La cache jejeje\n\n\n')
            print(f"[Error] An exception occurred in Main: {str(e)}")
            # handle the exception here, or re-raise it if necessary
        except PostUUTException as e:
            print(f"[Error] An exception occurred in PostUUT: {str(e)}")
            # handle the exception here, or re-raise it if necessary
        except PostUUTLoopException as e:
            print(f"[Error] An exception occurred in PostUUTLoop: {str(e)}")
            # handle the exception here, or re-raise it if necessary
        except Exception as e:
            print(f"[Error] Unhandled exception occurred: {str(e)}")
            # handle the exception here, or re-raise it if necessary
    return wrapper


def exceptions_handler_preuutloop(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #print(f"[Error] An exception occurred in PreUUTLoop: {str(e)}")
            raise PreUUTLoopException(e)
            # handle the exception here, or re-raise it if necessary
    return wrapper


def exceptions_handler_preuut(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #print(f"[Error] An exception occurred in PreUUT: {str(e)}")
            raise PreUUTException(e)
            # handle the exception here, or re-raise it if necessary
    return wrapper


def exceptions_handler_main(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #print(f"[Error] An exception occurred in Main: {str(e)}")
            raise MainException(str(e))
            # handle the exception here, or re-raise it if necessary
    return wrapper


def exceptions_handler_postuut(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #print(f"[Error] An exception occurred in PostUUT: {str(e)}")
            raise PostUUTException(e)
            # handle the exception here, or re-raise it if necessary
    return wrapper


def exceptions_handler_postuutloop(func):
    ''' Decorator to handle all exceptions on process model'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            #print(f"[Error] An exception occurred in PostUUTLoop: {str(e)}")
            raise PostUUTLoopException(e)
            # handle the exception here, or re-raise it if necessary
    return wrapper