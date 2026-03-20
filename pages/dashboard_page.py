"""
Dashboard Page Object Model for HR Orange Application.

This module provides the DashboardPage class that encapsulates all interactions
with the dashboard page of the HR Orange application.
"""

from playwright.sync_api import Page, Locator, expect


class DashboardPage:
    """
    Page Object for the Dashboard Page.
    
    The dashboard page is displayed after successful login and serves as the
    main landing page for authenticated users.
    
    Attributes:
        page (Page): Playwright page instance for browser interactions
    """
    
    def __init__(self, page: Page):
        """
        Initialize DashboardPage with a Playwright page instance.
        
        Args:
            page (Page): Playwright page object
        """
        self.page = page
    
    @property
    def profile_image(self) -> Locator:
        """
        Get the user profile image locator.
        
        Returns:
            Locator: Playwright locator for the profile picture in the header
        """
        return self.page.locator("//li//img[@alt='profile picture']")
    
    def ensure_page_loaded(self):
        """
        Ensure the dashboard page is fully loaded and displayed.
        
        Validates that key elements of the top header strip are visible:
        - Dashboard title (heading)
        - Upgrade button
        - Username profile image
        
        Raises:
            AssertionError: If any of the key elements are not visible
        """
        # Verify dashboard title is visible
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()
        
        # Verify upgrade button is visible (note the leading space in button text)
        expect(self.page.get_by_role("button", name=" Upgrade")).to_be_visible()
        
        # Verify username profile image is visible
        expect(self.profile_image).to_be_visible()
