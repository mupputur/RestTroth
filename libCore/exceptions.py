from libCore.constants import  (HTTP_BAD_REQUEST,
                                HTTP_CONFILCT,
                                HTTP_FORBIDDEN,
                                HTTP_INTERNAL_SERVER_ERROR,
                                HTTP_NOT_FOUND,
                                HTTP_SERVICE_UNAVAILABLE,
                                HTTP_UNAUTHORIZED,
                                HTTP_TOO_MANY_REQUESTS)


def get_error_message(response):
    try:
        json_obj = response.json()
        message = json_obj['message'] if 'message' in json_obj else json_obj
    except (KeyError, ValueError):
        message = response

    return message


class HTTPException(Exception):
    def __init__(self, response):
        super(HTTPException, self).__init__(get_error_message(response))


class BadRequestException(HTTPException):
    def __init__(self, response):
        super(BadRequestException, self).__init__(response)


class UnauthorizedException(HTTPException):
    def __init__(self, response):
        super(UnauthorizedException, self).__init__(response)


class ForbiddenException(HTTPException):
    def __init__(self, response):
        super(ForbiddenException, self).__init__(response)


class NotFoundException(HTTPException):
    def __init__(self, response):
        super(NotFoundException, self).__init__(response)


class ConflictException(HTTPException):
    def __init__(self, response):
        super(ConflictException, self).__init__(response)


class InternalServerErrorException(HTTPException):
    def __init__(self, response):
        super(InternalServerErrorException, self).__init__(response)


class ServiceUnavailableException(HTTPException):
    def __init__(self, response):
        super(ServiceUnavailableException, self).__init__(response)


class TooManyRequestsException(HTTPException):
    def __init__(self, response):
        super(TooManyRequestsException, self).__init__(response)


def get_http_exceptions(status_code):
    return {
        HTTP_BAD_REQUEST: BadRequestException,
        HTTP_CONFILCT: ConflictException,
        HTTP_FORBIDDEN: ForbiddenException,
        HTTP_INTERNAL_SERVER_ERROR: InternalServerErrorException,
        HTTP_NOT_FOUND: NotFoundException,
        HTTP_SERVICE_UNAVAILABLE: ServiceUnavailableException,
        HTTP_UNAUTHORIZED: UnauthorizedException,
        HTTP_TOO_MANY_REQUESTS: TooManyRequestsException
    }.get(status_code, HTTPException)


if __name__ == "__main__":
    pass
