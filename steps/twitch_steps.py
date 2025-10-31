from pathlib import Path
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.streamer_page import StreamerPage
from pages.popups import Popups
from utils.page_actions import PageActions
from utils.steps_decorator import step

"""
Steps for reuse in tests
"""

@step("Open Twitch homepage")
def open_home(page: Page, base_url: str) -> HomePage:
    home = HomePage(page)
    return home.goto_home(base_url)


@step("Dismiss popups on current page")
def dismiss_popups(page: Page) -> None:
    Popups(page).dismiss_popups()


@step("Assert home is loaded")
def assert_home_loaded(home: HomePage) -> None:
    assert home.is_loaded(), "Home page did not load correctly"


@step("Search for term and submit")
def search_term(home: HomePage, term: str) -> SearchResultsPage:
    return home.open_search().type_search_and_submit(term)


@step("Scroll results")
def scroll_results(page: Page, times: int) -> None:
    PageActions(page).scroll_down(times)


@step("Wait results DOM ready")
def wait_results_ready(results: SearchResultsPage) -> None:
    results.wait_dom_ready()


@step("Select first live streamer")
def select_first_streamer(results: SearchResultsPage) -> StreamerPage:
    return results.select_first_streamer()


@step("Wait for streamer video to be ready")
def wait_video_ready(streamer: StreamerPage) -> None:
    streamer.wait_for_video()


@step("Take final streamer screenshot")
def take_final_screenshot(page: Page, name: str = "streamer_page.png") -> Path:
    return PageActions(page).take_screenshot(name)


