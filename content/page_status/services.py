from content.page.models import Page


class PageCMSStatusService:
    @staticmethod
    def get_available_status_page(*, page: Page) -> list:
        available_status = {
            Page.StatusChoices.NEW_DRAFT.value: [
                Page.StatusChoices.TO_PUBLISH,
            ],
            Page.StatusChoices.TO_PUBLISH.value: [
                Page.StatusChoices.TO_PUBLISH,
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

    def changes_status_page(self, page: Page, new_status: int):
        if new_status in self.get_available_status_page(page=page):
            page.status = new_status
            page.save()
