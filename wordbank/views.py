from django.http import HttpResponse


class HttpResponseNoContent(HttpResponse):
    """
    Special HTTP response with no content, just headers.
    The content operations are ignored.
    """

    def __init__(self, content="", mimetype=None, status=None, content_type=None):
        super().__init__(status=204)

        if "content-type" in self._headers:
            del self._headers["content-type"]

    def _set_content(self, value):
        pass

    def _get_content(self, value):
        pass


def health_view(request):
    return HttpResponseNoContent()
