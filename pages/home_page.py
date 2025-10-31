from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage
from pages.popups import Popups
from locators.home_locators import HomeLocators


class HomePage(BasePage):
    """
    Page Object for homepage
    """

    _BROWSE_BUTTON = HomeLocators.BROWSE_BUTTON
    _SEARCH_INPUT = HomeLocators.SEARCH_INPUT

    def goto_home(self, url: str) -> "HomePage":
        super().goto(url)
        Popups(self.page).dismiss_popups()
        return self

    def is_loaded(self) -> bool:
        return self.is_visible(self._BROWSE_BUTTON)

    def open_search(self) -> "HomePage":
        self.click(self._BROWSE_BUTTON)
        return self

    def type_search_and_submit(self, term: str) -> "SearchResultsPage":
        input_box = self.wait_until_visible(self._SEARCH_INPUT)
        input_box.fill(term)
        input_box.press("Enter")
        return SearchResultsPage(self.page)
