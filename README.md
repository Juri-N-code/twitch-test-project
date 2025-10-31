## Twitch Tests (Playwright + Pytest)

This is a test assignment demonstrating an end-to-end mobile user flow on Twitch using Python, Playwright, and Pytest. 
The test searches for a Starcraft streamer, opens live video and captures a screenshot. 
The project follows the Page Object Model (POM), stores run artifacts (traces and screenshots).

### Repository Structure
```
.
├── config/
│   └── settings.py            # Global settings
├── pages/
│   ├── base_page.py           # Common page helpers
│   ├── home_page.py           # Twitch homepage POM
│   ├── search_results_page.py # Search results POM
│   ├── streamer_page.py       # Streamer page POM
│   └── popups.py              # Popups helper
├── tests/
│   └── test_twitch_mobile.py  # Main E2E scenario
├── testdata/
│   └── twitch_search.json     # Test data
├── utils/
│   ├── data_loader.py         # Helper for loading test data from JSON
│   └── page_actions.py        # Page actions helpers
├── conftest.py                # Pytest fixtures
├── pytest.ini                 # Pytest config
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── test-results/              # Run artifacts
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
