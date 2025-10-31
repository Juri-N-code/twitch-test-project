import pytest
import logging
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.popups import Popups
from utils.data_loader import load_json
from utils.page_actions import PageActions

logger = logging.getLogger(__name__)


@pytest.mark.e2e
def test_twitch_mobile_starcraft(page: Page, twitch_entrypoint: str) -> None:
    """
    E2E test: user opens Twitch, searches for a StarCraft ii streamer,
    selects first one, waits until stream loads, and takes a screenshot.
    """

    # Setup test data
    data = load_json("twitch_search.json")
    search_term = data.get("searchTerm")
    scroll_times = int(data.get("scrollTimes"))

    # Actions
    logger.info("Opening Twitch home page")
    home = HomePage(page)
    home.goto_home(twitch_entrypoint)
    Popups(page).dismiss_popups()
    assert home.is_loaded(), "Home page did not load correctly"

    logger.info(f"Searching for term: {search_term}")
    search_results = home.open_search().type_search_and_submit(search_term)

    logger.info(f"Scrolling {scroll_times} times to load more results")
    PageActions(search_results.page).scroll_down(scroll_times)
    search_results.wait_dom_ready()

    logger.info("Selecting the first streamer from results")
    streamer_page = search_results.select_first_streamer()
    logger.info("Closing any popups on streamer page")
    Popups(page).dismiss_popups()
    streamer_page.wait_for_video()

    # Assertions
    logger.info("Taking screenshot of the streamer page")
    screenshot_path = PageActions(streamer_page.page).take_screenshot("streamer_page.png")
    assert screenshot_path.exists(), f"Screenshot file not found at {screenshot_path}"

    logger.info("Test finished successfully.")
