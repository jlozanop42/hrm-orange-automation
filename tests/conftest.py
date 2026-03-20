"""
pytest configuration file for HR Orange Automation Framework.

This file uses pytest-playwright plugin which provides built-in fixtures:
- playwright: Playwright instance
- browser: Browser instance (controlled by --browser option)
- context: Browser context for test isolation
- page: Page instance for browser interactions

Usage:
    pytest                                 # Run all tests (chromium, headless)
    pytest --browser chromium              # Explicitly use Chromium
    pytest --browser firefox               # Run tests in Firefox
    pytest --browser webkit                # Run tests in WebKit (Safari)
    pytest --headed                        # Run with visible browser window
    pytest --headed --browser firefox      # Combine options
    pytest --slowmo 1000                   # Slow down operations by 1 second
"""
