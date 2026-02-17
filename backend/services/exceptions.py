class ServiceErrors(Exception):
    pass

# Uploads
class UploadedFileDoesNotExist(ServiceErrors):
    def __init__(self, message):
        super().__init__(message)

class HttpxRequestError(ServiceErrors):
    def __init__(self, message):
        super().__init__(message)

# URL Ingest
class ResourceURLDoesNotExist(ServiceErrors):
    def __init__(self, message):
        super().__init__(message)

# YT Transcript
class YTVideoDoesNotExist(ServiceErrors):
    def __init__(self, message):
        super().__init__(message)
