import pytest
from pathlib import Path
from playwright.sync_api import Page
from utils.data_loader import load_json
from steps.twitch_steps import (
    open_home,
    dismiss_popups,
    assert_home_loaded,
    search_term,
    scroll_results,
    wait_results_ready,
    select_first_streamer,
    wait_video_ready,
    take_final_screenshot,
)


@pytest.mark.e2e
def test_twitch_mobile_starcraft(page: Page, twitch_entrypoint: str) -> None:
    data = load_json("twitch_search.json")
    term = data.get("searchTerm")
    times = int(data.get("scrollTimes"))

    home = open_home(page, twitch_entrypoint)
    dismiss_popups(page)
    assert_home_loaded(home)

    results = search_term(home, term)
    scroll_results(results.page, times)
    wait_results_ready(results)

    streamer = select_first_streamer(results)
    dismiss_popups(page)
    wait_video_ready(streamer)

    path: Path = take_final_screenshot(streamer.page, "streamer_page.png")
    assert path.exists()
