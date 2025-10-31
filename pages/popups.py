from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class Popups:
    """
    Class for closing popups
    """

    _POPUPS_SELECTORS = [
        ".popup-selector",
        "div[role='dialog']",
        "button[aria-label='Close']"
    ]

    def __init__(self, page: Page) -> None:
        self.page = page

    def dismiss_popups(self) -> None:
        logger.info("Closing popups")
        for selector in self._POPUPS_SELECTORS:
            try:
                locator = self.page.locator(selector)
                if locator.count() > 0:
                    locator.first.wait_for(state="visible", timeout=500)
                    locator.first.click()
                    logger.info(f"Dismissed popup with selector: {selector}")
            except TimeoutError:
                continue
            except Exception as e:
                logger.error(f"Failed to dismiss popup {selector}: {e}")

        # Fallback: press Escape 
        try:
            self.page.keyboard.press("Escape")
            logger.info("Pressed Escape to dismiss any remaining popups")
        except Exception:
            pass
