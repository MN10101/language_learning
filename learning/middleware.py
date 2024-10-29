from django.utils.deprecation import MiddlewareMixin
from datetime import datetime, timedelta

class DisableCacheMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = (datetime.now() + timedelta(minutes=5)).strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response