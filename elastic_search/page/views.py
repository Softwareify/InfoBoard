from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import PageDocument
from .serializers import PageDocumetSerializer
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    FilteringFilterBackend,
)


class PageDocumentView(DocumentViewSet):
    document = PageDocument
    serializer_class = PageDocumetSerializer

    filter_backends = [SearchFilterBackend, FilteringFilterBackend]

    search_fields = ("name", "description")

    filter_fields = {"slug": "slug.id"}
