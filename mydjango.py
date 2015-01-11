from functools import wraps
import json
from django.http.response import HttpResponse, HttpResponseNotAllowed


class JSONResponse(HttpResponse):
    def __init__(self, obj):
        super(JSONResponse, self).__init__(json.dumps(obj), content_type='application/json')
