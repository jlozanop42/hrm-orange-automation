"""
Configuration management for HR Orange Automation Framework.

This module provides centralized configuration using environment variables,
allowing different settings for various test environments (QA, Staging, Production).
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """
    Configuration dataclass for test environment settings.
    
    All settings can be overridden using environment variables, making it easy
    to configure different test environments without changing code.
    
    Attributes:
        BASE_URL (str): Base URL of the application under test
        HEADLESS (bool): Whether to run browser in headless mode
        TIMEOUT (int): Default timeout in milliseconds for Playwright actions
        BROWSER (str): Browser to use (chromium, firefox, or webkit)
    
    Environment Variables:
        BASE_URL: Override the default application URL
        HEADLESS: Set to "false" to run browser in headed mode
        TIMEOUT: Override default timeout (in milliseconds)
        BROWSER: Choose browser (chromium, firefox, webkit)
    
    Examples:
        # Use default settings
        from utils.config import config
        page.goto(config.BASE_URL)
        
        # Override via environment variables
        export BASE_URL="https://qa.orangehrmlive.com"
        export HEADLESS="false"
        pytest tests/
    """
    
    BASE_URL: str = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30000"))
    BROWSER: str = os.getenv("BROWSER", "chromium")


# Singleton instance to be imported throughout the framework
config = Config()
