class TransferWiseAPIException(Exception):

    def __init__(self, response):
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = f"Invalid JSON error message from TransferWise: {response.text}"
        else:
            self.code = json_res['code']
            self.message = json_res['msg']
        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return 'APIError(code=%s): %s' % (self.code, self.message)


class TransferWiseRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'TransferWiseRequestException: %s' % self.message
