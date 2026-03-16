"""
pytest configuration file for HR Orange Automation Framework.

This file provides fixtures for Playwright browser automation and test configuration.
"""

import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext, Page


def pytest_addoption(parser):
    """
    Add custom command-line options for pytest.
    
    Usage:
        pytest --browser chromium
        pytest --browser firefox
        pytest --browser webkit
        pytest --headed  # Run in headed mode (visible browser) mmmm
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, or webkit",
        choices=["chromium", "firefox", "webkit"],
    )
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode (visible browser window)",
    )


@pytest.fixture(scope="session")
def browser_name(request) -> str:
    """
    Get the browser name from command-line argument.
    
    Returns:
        str: Browser name (chromium, firefox, or webkit)
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def is_headed(request) -> bool:
    """
    Get the headed mode setting from command-line argument.
    
    Returns:
        bool: True if headed mode is enabled, False otherwise
    """
    return request.config.getoption("--headed")


@pytest.fixture(scope="session")
def playwright_browser(playwright: Playwright, browser_name: str, is_headed: bool) -> Browser:
    """
    Launch the browser based on the selected browser type.
    
    Args:
        playwright: Playwright instance (provided by pytest-playwright plugin)
        browser_name: Browser type from CLI argument
        is_headed: Whether to run in headed mode
    
    Returns:
        Browser: Playwright browser instance
    """
    headless = not is_headed
    
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=headless)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(playwright_browser: Browser) -> BrowserContext:
    """
    Create a new browser context for each test.
    
    Browser contexts are isolated environments within a browser instance.
    Each test gets a fresh context to ensure test isolation.
    
    Args:
        playwright_browser: Browser instance
    
    Returns:
        BrowserContext: Isolated browser context
    """
    context = playwright_browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True,
    )
    
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """
    Create a new page for each test.
    
    This is the main fixture that tests will use to interact with the browser.
    
    Args:
        context: Browser context
    
    Returns:
        Page: Playwright page object for browser interaction
    """
    page = context.new_page()
    
    yield page
    page.close()
