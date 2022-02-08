
class JPApiError(Exception):
    def __init__(self, message, status_code=500, **kwargs):
        self.message = message
        self.status_code = status_code
        self.response = kwargs.get("response", None)

    def __str__(self):
        return self.message
