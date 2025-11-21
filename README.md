## Twitch Tests (Playwright + Pytest)

This is a test assignment demonstrating an end-to-end mobile user flow on Twitch using Python, Playwright, and Pytest. 
The test searches for a Starcraft streamer, opens live video and captures a screenshot. 
The project follows the Page Object Model (POM), stores run artifacts (traces and screenshots). 

**TODO:** Improve configu ration management to support multiple browsers and devices,
for instance with command line parameters (pytest --browser=firefox --device="iPhone 12"),
making easier cross-browser/device testing.

### Repository Structure
```
.
├── config/                        # Сonfig storage
│   └── settings.py                # Global settings (URL, timeouts, devices) - single point for configuration
├── locators/                      # Separation locators from page logic for better maintainability
│   ├── home_locators.py           # 
│   ├── popups_locators.py         # 
│   ├── search_results_locators.py # 
│   └── streamer_locators.py       # 
├── pages/                         # Page Object Model to encapsulate page interactions
│   ├── base_page.py               # Base class with common methods
│   ├── home_page.py               # 
│   ├── search_results_page.py     # 
│   ├── streamer_page.py           # 
│   └── popups.py                  # Separate class for popups, reusable across pages
├── steps/                         # Reusable steps for composing test scenarios
│   └── twitch_steps.py            # Atomic steps (open home, search, scroll), can be reused in multiple tests
├── tests/                         # Test scenarios
│   └── test_twitch_mobile.py      # Main E2E test
├── testdata/                      # Separation of test data from code for easy modification
│   └── twitch_search.json         # JSON with with test parameters easy to change without code edits
├── utils/                         # Helper utilities for reuse
│   ├── data_loader.py             # Load JSON data
│   ├── page_actions.py            # Common page actions for reuse 
│   └── steps_decorator.py         # Decorator for step logging or Allure integration
├── conftest.py                    # Pytest fixtures for setup/teardown
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies 
├── README.md                      # This file
└── test-results/                  # Run artifacts
```

---

### Requirements
- Python 3.10+
- Google Chrome
- Playwright 1.48.x

---

### Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### Running Tests
Basic run from the project root:
```bash
pytest
```

---

![Run GIF](run.gif)
