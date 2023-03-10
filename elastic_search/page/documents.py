from django_elasticsearch_dsl import fields, Document
from django_elasticsearch_dsl.registries import registry

from content.page.models import Page


@registry.register_document
class PageDocument(Document):
    name = fields.TextField(
        attr="name", fields={
            "raw": fields.TextField(),
            "suggest": fields.CompletionField()
        }
    )
    slug = fields.TextField(
        attr="slug", fields={
            "raw": fields.TextField(),
            "suggest": fields.CompletionField()
        }
    )
    description = fields.TextField(
        attr="description", fields={
            "suggest": fields.Completion()
        }
    )

    class Index:
        name = "pages"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }

    class Django:
        model = Page