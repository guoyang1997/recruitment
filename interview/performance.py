import time
import logging

from django.http.response import HttpResponseBase

logger = logging.getLogger(__name__)

def performance_logger_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()
        duration = end_time - start_time
        response["X-Page-Duration-ms"] = int(duration*1000)
        logger.info("%s %s %s",duration,request.path,request.GET.dict())

        return response
    return middleware