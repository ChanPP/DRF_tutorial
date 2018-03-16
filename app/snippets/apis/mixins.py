from rest_framework import mixins, generics

from snippets.serializers import SnippetSerializer
from ..models import Snippet

__all__ = (
    "SnippetList",
    "SnippetDetail",
)


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, request, *args, **kwargs)


class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    generics.DestroyAPIView, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
