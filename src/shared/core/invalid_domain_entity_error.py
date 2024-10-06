from shared.core.application_error import ApplicationError


class InvalidDomainEntityError(ApplicationError):
    def __init__(self, message: str):
        super().__init__(message)