import json

from django.http import HttpResponse

from abstract_controller import AbstractController


class SampleController(AbstractController):
    @classmethod
    def read(cls, request):
        # For example read a list of objects from database and return json encoded response
        return HttpResponse(json.dumps([1, 2, 3]))
