import inspect

from django.conf.urls import url


class AbstractController(object):
    @classmethod
    def getUrls(cls):
        public_methods = inspect.getmembers(cls, inspect.ismethod)
        return [url(r"^%s$" % (x[0]), x[1]) for x in public_methods]

    @classmethod
    def testAction(cls, request):
        # do something useful
        pass
