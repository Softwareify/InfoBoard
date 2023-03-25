from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from elastic_search.page.documents import PageDocument


class PageDocumetSerializer(DocumentSerializer):
    class Meta:
        document = PageDocument

        fields = ("name", "slug", "description")
