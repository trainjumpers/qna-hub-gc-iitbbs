import json
from typing import List, Any, Dict

from fastapi import Request


class APIException(Exception):
    """Custom global exception for all of our APIs. It is to be used with a try catch that surrounds the core api logic.
    This takes the logic for failed exceptions and formats it for all. 
    Attributes:
        trace: string formatted traceback of the original exception.
        body: request body as a dict. Defaults to an empty json object.
    Methods:
        get_context_dict: Creates a dict containing the response body for all internal server errors.
        format_exception_trace: Formats the provided string trace into a list of strings.
    """

    def __init__(self, trace: str, body: str = "{}"):
        self.trace = trace
        self.body = json.loads(body)
        super(APIException, self).__init__()

    def get_context_dict(self, request: Request) -> Dict[str, Any]:
        trace: List[str] = self.format_exception_trace(self.trace)
        return {
            "message": trace.pop(),
            "stacktrace": trace,
            "request": {
                "api": "/" + str(request.url).lstrip(str(request.base_url)),
                "method": request.method,
                "body": self.body
            }
        }

    @staticmethod
    def format_exception_trace(trace: str) -> List[str]:
        """
        Args:
            trace: string formatted traceback of the original exception.
        Returns:
            formatted_trace: list of processed strings representing the trace
        """

        return list(filter(lambda x: x and x != "", map(lambda x: x.strip().replace('\"', ''), trace.split('\n'))))[1:]