from playwright.sync_api import Page, expect
from config import settings


class BasePage:
    """
    Base class for all pages
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def wait_dom_ready(self):
        self.page.wait_for_load_state("domcontentloaded")

    def wait_until_visible(self, locator: str, timeout: int = settings.DEFAULT_TIMEOUT_MS):
        element = self.page.locator(locator)
        expect(element).to_be_visible(timeout=timeout)
        return element

    def click(self, locator: str, timeout: int = settings.DEFAULT_TIMEOUT_MS):
        self.wait_until_visible(locator, timeout)
        self.page.locator(locator).click()

    def is_visible(self, locator: str, timeout: int = settings.DEFAULT_TIMEOUT_MS) -> bool:
        try:
            expect(self.page.locator(locator)).to_be_visible(timeout=timeout)
            return True
        except Exception:
            return False
