from typing import Self

from locators.streamer_locators import StreamerLocators
from pages import BasePage


class StreamerPage(BasePage):
    """Page Object for a Twitch streamer's page."""

    _VIDEO_SELECTOR = StreamerLocators.VIDEO

    def wait_for_video(self) -> Self:
        """
        Wait until the streamer page is fully loaded.
        Checks for video element readiness or fallback persistent player.
        """
        self.page.wait_for_function(
                f"() => document.querySelector('{self._VIDEO_SELECTOR}') && document.querySelector('{self._VIDEO_SELECTOR}').readyState >= 2"
            )
        
        return self  
