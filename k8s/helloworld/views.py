# from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    http_method_names = ['get']

    def get(self, request, format=None):
        # cache.set("test_key", "123456", 3600)
        # content = {
        #     "value": cache.get('test_key')
        # }
        content = {"value": "Hello World."}
        return Response(content, 200)
