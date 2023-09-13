from content.page.models import Page


class PageCMSStatusService:
    model = Page

    @staticmethod
    def get_available_status_page(*, page: Page) -> list:
        available_status = {
            Page.StatusChoices.NEW_DRAFT.value: [
                Page.StatusChoices.TO_PUBLISH,
            ],
            Page.StatusChoices.TO_PUBLISH.value: [
                Page.StatusChoices.PUBLISHED,
            ],
            Page.StatusChoices.PUBLISHED.value: [
                Page.StatusChoices.NEW_DRAFT,
                Page.StatusChoices.TO_ARCHIVE,
            ],
            Page.StatusChoices.ARCHIVE.value: [
                Page.StatusChoices.NEW_DRAFT,
            ],
        }
        return available_status.get(page.status, None)

    @classmethod
    def changes_status_page(cls, page: Page, new_status: int):
        from publisher.services import PublicationService

        if new_status in cls.get_available_status_page(page=page):
            if new_status is Page.StatusChoices.TO_PUBLISH.value:
                PublicationService.add_task(
                    type_publication="page_publish",
                    object_id=page.id,
                    due_date=page.publish_from,
                )
            page.status = new_status
            page.save()
