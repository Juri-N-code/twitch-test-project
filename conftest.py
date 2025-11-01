import pathlib
from datetime import datetime, UTC
import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright

from config import settings

TRACE_FILE_NAME = "trace.zip"


@pytest.fixture(scope="session")
def playwright_instance() -> Playwright:
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    return playwright_instance.chromium.launch(
        channel="chrome",
        headless=False,
    )


@pytest.fixture(scope="session")
def device(playwright_instance: Playwright) -> dict:
    return playwright_instance.devices.get(settings.MOBILE_DEVICE_NAME)


@pytest.fixture(scope="function")
def context(
        browser: Browser,
        device: dict,
        request: pytest.FixtureRequest,
        run_id: str,
) -> BrowserContext:
    base_artifacts_root = pathlib.Path(settings.ARTIFACTS_DIR)
    run_root = base_artifacts_root / run_id
    test_root = run_root / request.node.name

    try:
        from config import settings as mutable_settings
        mutable_settings.SCREENSHOTS_DIR = str(test_root)
    except Exception:
        pass

    context_options = {
        **device,
        "locale": settings.LOCALE,
        "color_scheme": settings.COLOR_SCHEME,
    }
    # Tracing
    ctx = browser.new_context(**context_options)
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield ctx

    trace_path = test_root / TRACE_FILE_NAME
    try:
        ctx.tracing.stop(path=trace_path)
    finally:
        ctx.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    page.set_default_timeout(settings.DEFAULT_TIMEOUT_MS)
    return page


@pytest.fixture(scope="session")
def twitch_entrypoint() -> str:
    return settings.BASE_URL


@pytest.fixture(scope="session")
def run_id() -> str:
    """
    Unique identifier for the test session
    """
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    return f"run-{ts}"
