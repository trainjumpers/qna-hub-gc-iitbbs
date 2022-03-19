class ResourceNotFoundException(Exception):
    pass


class UserNotFoundException(ResourceNotFoundException):

    def __init__(self, email: str):
        message = f"User with email: {email} does not exist"
        super(UserNotFoundException, self).__init__(message)


class UserUnauthorizedException(Exception):

    def __init__(self, message: str):
        super(UserUnauthorizedException, self).__init__(message)


class ResourceConflictException(Exception):

    def __init__(self, message: str):
        super(ResourceConflictException, self).__init__(message)