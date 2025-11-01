import logging
from pathlib import Path

from playwright.sync_api import Page

from config import settings

logger = logging.getLogger(__name__)


class PageActions:
    """
    Helper methods for page interactions
    """

    def __init__(self, page: Page):
        self.page = page

    def scroll_down(self, times: int = 1, step: int = 2000, delay_ms: int = 800):
        """
        Scroll down several times
        """
        logger.debug(f"Scrolling down {times} times (step={step}, delay={delay_ms}ms)")
        for _ in range(times):
            self.page.mouse.wheel(0, step)
            self.page.wait_for_timeout(delay_ms)

    def take_screenshot(self, name: str) -> Path:
        """
        Take a screenshot of the current page and save to out_dir with name.
        Returns Path to the screenshot file.
        """
        out_path = Path(settings.SCREENSHOTS_DIR)
        out_path.mkdir(parents=True, exist_ok=True)
        file_path = out_path / name
        self.page.screenshot(path=file_path, full_page=False)
        return file_path
