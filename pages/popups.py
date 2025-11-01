import logging

from playwright.sync_api import Page

from locators.popups_locators import PopupsLocators

logger = logging.getLogger(__name__)


class Popups:
    """
    Class for closing popups
    """

    _POPUPS_SELECTORS = PopupsLocators.CANDIDATES

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

        self.page.keyboard.press("Escape")
        logger.info("Pressed Escape to dismiss any remaining popups")
