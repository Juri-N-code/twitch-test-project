from pages.streamer_page import StreamerPage
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    """
    Page Object for the search results page
    """

    _LIVE_BUTTON = 'button:has(span:text("Live"))'

    def select_first_streamer(self) -> "StreamerPage":
        """
        elect the first 'Live' streamer
        """
        live_element = self.page.locator(self._LIVE_BUTTON).first
        live_element.scroll_into_view_if_needed()
        live_element.click()
        return StreamerPage(self.page)
